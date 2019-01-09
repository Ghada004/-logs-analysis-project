import psycopg2

# Connect to database and setup cursor
connection = psycopg2.connect("dbname=news")
cursor = connection.cursor()


# The most popular three articles of all time

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
    SELECT *
    FROM errPercentage0
     WHERE errPercentage0.percentage > 1
     ORDER BY errPercentage0.percentage DESC;
    """

    cursor.execute(query)
    return cursor.fetchall()
    db.close()

# Print out put


query01 = popularArticle()
query02 = popularAuthors()
query03 = errorsRequests()


print(
    '\nMost three popular articles:')
for(title, count) in query01:
    print(" {} - {} views".format(title.replace('-', ' ').capitalize(), count))

print(
    '\nMost popular author:\n' +
    ' %s - %d views\n' % (query02[0][0], query02[0][1]))

print(
    '\nDays with more than one percentage of bad requests:')
print((str(query03[0][1])) + ' - ' + str(query03[0][2]) + ' %')
