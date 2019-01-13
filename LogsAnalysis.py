#!/usr/bin/env python
psycopg2
from datetime import datetime


# Connect to database and setup cursor
connection = psycopg2.connect("dbname=news")
cursor = connection.cursor()


# The most popular three articles of all time

def popularArticle():
    query1 = """
            SELECT articles.title, count(*)
            From articles JOIN log
            ON CONCAT('/article/', articles.slug) = log.path
            GROUP BY articles.title
            ORDER BY count(*) DESC
            LIMIT 3;
    """
    cursor.execute(query1)
    print("\nMost three popular articles:\n")
    for(title, count) in cursor.fetchall():
        print(" {} - {} views".format(title, count))


# The most popular article authors of all time
def popularAuthors():
    query2 = """
             SELECT authors.name, count(*)
             FROM articles
             JOIN authors
             ON authors.id = articles.author
             JOIN log
             ON CONCAT('/article/', articles.slug) = log.path
             GROUP BY authors.name
             ORDER BY count(*) DESC
    """
    cursor.execute(query2)
    print("\nMost popular author:\n")
    for(name, count) in cursor.fetchall():
        print(" {} - {} views".format(name, count))


# On which days did more than 1% of requests lead to errors
def errorsRequests():

    query3 = """
    SELECT *
    FROM errPercentage0
     WHERE errPercentage0.percentage > 1
     ORDER BY errPercentage0.percentage DESC
     LIMIT 1;
    """
    cursor.execute(query3)
    print("\nDays with more than one percentage of bad requests:\n")
    for q3 in cursor.fetchall():
        print((q3[1]).strftime("%B %d, %Y") + " - " + str(q3[2]) + " % errors")

    connection.close()
    cursor.close()


if __name__ == '__main__':
    popularArticle()
    popularAuthors()
    errorsRequests()
