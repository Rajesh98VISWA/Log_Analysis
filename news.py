#!/usr/bin/env python3
import psycopg2

from datetime import datetime

query_1 = ("SELECT a.title, count(*) AS views "
           "FROM articles a INNER JOIN log b "
           "on a.slug=replace(path,'/article/','') "
           "WHERE status='200 OK' AND length(path)>1 GROUP by "
           "a.title ORDER by views DESC limit 3")

query_2 = ("SELECT c.name, count(*) AS views "
           "FROM articles a INNER JOIN log b "
           "on a.slug=replace(path,'/article/','') INNER JOIN "
           "authors c on (c.id=a.author) "
           "WHERE status='200 OK' AND length(path)>1 GROUP by "
           "c.name ORDER by views DESC")

query_3 = """WITH num_requests AS (
	SELECT time::date AS day, count(*)
	FROM log
	GROUP BY time::date
	ORDER BY time::date
	), num_errors AS (
	SELECT time::date AS day,count(*)
	FROM log
	WHERE status != '200 OK'
	GROUP BY time::date
	ORDER BY time::date
	), error_rate AS (
	SELECT num_requests.day ,
	 num_errors.count::float /num_requests.count::float *100
	 AS error_pc
	FROM num_requests,num_errors
	WHERE num_requests.day = num_errors.day
	)
	SELECT * FROM error_rate WHERE error_pc > 1;
	"""


def f():
    d = psycopg2.connect("dbname=news")
    cur = d.cursor()
    cur.execute(query_1)
    results = cur.fetchall()
    print("Most Popular Articles")
    for result in results:
        print('"{title}" - {count} views'.format(title=result[0], count=result[1])+ "\n")

    cur.execute(query_2)
    results = cur.fetchall()
    print("Most Popular authors")
    for result in results:
        print('{author} - {count} views'.format(
            author=result[0], count=result[1])+"\n")

    cur.execute(query_3)
    results = cur.fetchall()
    print("Days in Which More Than One Percent of Error")
    for result in results:
    	print('{date:%B %d, %Y}-{error_rate:.1f}% errors'.format(date=result[0],error_rate=result[1]))
    	cur.close()
    	d.close()

if __name__ == '__main__':
    f()
