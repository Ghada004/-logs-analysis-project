import psycopg2

# Connect to database and setup cursor
connection = psycopg2.connect("dbname=news")
cursor = connection.cursor()

# The most popular article authors of all time


def popularArticle():
    query = """
            SELECT articles.title, count(*)
            From articles JOIN log
            ON CONCAT('/article/', articles.slug) = log.path
            GROUP BY articles.title
            ORDER BY count(*) DESC
            LIMIT 3;
    """
    cursor.execute(query)
    return cursor.fetchall()
    db.close()

# The most popular article authors of all time


def popularAuthors():
    query = """
      	          SELECT authors.name, count(*)
                  FROM articles
                  JOIN authors
                  ON authors.id = articles.author
                  JOIN log
      	          ON CONCAT('/article/', articles.slug) = log.path
                  GROUP BY authors.name
                  ORDER BY count(*) DESC
    """
    cursor.execute(query)
    return cursor.fetchall()
    db.close()

# On which days did more than 1% of requests lead to errors


def errorsRequests():
    query = """

    """
    cursor.execute(query)
    return cursor.fetchall()
    db.close()

# Print out put

result01 = popularArticle()
result02 = popularAuthors()
result03 = errorsRequests()

print(
    'The most three popular articles:')
for(title, count) in result01:
    print(" {} - {} views".format(title.replace('-', ' ').capitalize(), count))

print(
    '\nThe most popular author:\n' +
    ' %s - %d views\n' % (result02[0][0], result02[0][1]))

print(
    'The days with error rate higher than 1'+'%:\n' + ' %s - %0.1f'
    % (result03[0][0].strftime('%B %d, %Y'), result03[0][1])+'%\n')
