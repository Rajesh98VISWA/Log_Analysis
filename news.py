#!/usr/bin/env python3
import psycopg2

# Answer1
PopularArticles = """
SELECT articles.title,
count(*)
FROM log,articles
WHERE log.path = '/article/' || articles.slug
GROUP BY articles.title
ORDER BY count(*) DESC
LIMIT 3;
"""
# Answer2
PopularAuthors = """
SELECT authors.name,
count(*)
FROM log,articles,authors
WHERE log.path = '/article/' || articles.slug
GROUP BY authors.name
ORDER BY count(*) DESC;
"""

# Answer3
MoreThanOnePercent = """
WITH num_requests AS (
SELECT Time::Date AS day, count(*)
FROM log
GROUP BY Time::Date
ORDER BY Time::Date
), num_errors AS (
SELECT Time::Date AS day,count(*)
FROM log 
WHERE status != '200 OK'
GROUP BY Time::Date
ORDER BY Time::Date
), error_rate AS (
SELECT num_requests.day ,
num_errors.count::float /num_requests.count::float *100
AS error_pc
FROM num_requests,num_errors
WHERE num_requests.day = num_errors.day
)
SELECT * FROM error_rate WHERE error_pc > 1;
"""


def Writer_checker():
    c = psycopg2.connect("dbname=news")
    blank = c.cursor()
### Popular Articles  execution

    blank.execute(PopularArticles)
    results = blank.fetchall()
    print("\n***Most--Popular--Articles***\n")
    for i in results:
        print(
            '"{title}"" - {count} views'.format(title=i[0], count=i[1]) 
            )
### Popular Authors execution

    blank.execute(PopularAuthors)
    results = blank.fetchall()
    print("\n***Most--Popular--Authors***\n")
    for i in results:
        print('{author} - {count} views'.format(author=i[0], count=i[1]))

### Days in which more than one percent error execution

    blank.execute(MoreThanOnePercent)
    results = blank.fetchall()
    print("\n***--Days in Which More Than One Percent Error--***\n")
    for i in results:
        print(
            '{date:%B %d, %Y}-{error_rate:.1f}% errors'.
            format(date=i[0], error_rate=i[1]))
    blank.close()
    c.close()

if __name__ == '__main__':
    Writer_checker()