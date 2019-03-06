#!/usr/bin/env python3
import psycopg2


def prototype():
    db = psycopg2.connect("dbname=news")
    temp = db.cursor()
    Articles = """
    SELECT title,count(*) as views FROM articles
    JOIN log
    ON articles.slug = substring(log.path, 10)
    GROUP BY title ORDER BY views DESC LIMIT 3;
    """
    temp.execute(Articles)
    final = temp.fetchall()
    print("Popular Articles\n")
    for i in final:
        print(
            '{title} - {count} views'.format(title=i[0], count=i[1])
            )
    print("\n")
    Authors = """
    SELECT authors.name,
    count(*)
    FROM log,articles,authors
    WHERE log.path = '/article/' || articles.slug
    GROUP BY authors.name
    ORDER BY count(*) DESC;
    """
    temp.execute(Authors)
    final = temp.fetchall()
    print("Popular Authors\n")
    for i in final:
        print('{author} - {count} views'.format(author=i[0], count=i[1]))
    print("\n")
    Error = """
    WITH num_req AS (
    SELECT time::date AS D, count(*)
    FROM log
    GROUP BY time::date
    ORDER BY time::date
    ), num_err AS (
    SELECT time::date AS D,count(*)
    FROM log
    WHERE status != '200 OK'
    GROUP BY time::date
    ORDER BY time::date
    ), error_rate AS (
    SELECT num_req.D ,
    num_err.count::float /num_req.count::float *100
    AS error_pc
    FROM num_req,num_err
    WHERE num_req.D = num_err.D
    )
    SELECT * FROM error_rate WHERE error_pc > 1;
    """
    temp.execute(Error)
    final = temp.fetchall()
    print("Days in Which More Than One Percent Error\n")
    for i in final:
        print(
            '{date:%B %d, %Y}-{error_rate:.1f}% errors'.
            format(date=i[0], error_rate=i[1])+"\n")
    temp.close()
    db.close()

if __name__ == '__main__':
    prototype()
