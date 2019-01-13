# A Udacity FSND project.


## logs analysis project
It's an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.

The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. Using that information, your code will answer questions about the site's user activity.

The program in this project will run from the command line. It won't take any input from the user. Instead, it will connect to that database, use SQL queries to analyze the log data, and print out the answers to some questions.

## What you need to RUN?
1/ Vagrant:	https://www.vagrantup.com/downloads.htmlb.VirtualMachine

2/ VirtualMachine:	https://www.virtualbox.org/wiki/Downloadsc.Download

3/ Download	a	FSND	VirtualMachine https://github.com/udacity/fullstack-nanodegree-vm

4/ Python https://www.python.org

## Database file

Download the newsdata.sql https://www.dropbox.com/s/dwwdrerml1nf0mf/newsdata.sql?dl=0

## How to RUN the Project
```
cd vagrant
vagrant up
vagrant ssh
cd /vagrant
cd log-analysis-project
python LogsAnalysis.py
```
### To load the data, cd into the vagrant directory and use the command psql -d news -f newsdata.sql.
### Here's what this command does:
```
psql — the PostgreSQL command line program
-d news — connect to the database named news which has been set up for you
-f newsdata.sql — run the SQL statements in the file newsdata.sql
```

### I used CREATE VIEW for The last Query.
##  How to access Database to CREATE VIEW  

## Once you have the data loaded into your database, connect to your database using:
```
psql -d news
```

## You can Explore the Data by:
```
 \dt: display tables — lists the tables that are available in the database 
 \d table_name: shows the database schema for that particular table
```

## The third Query Views

#1 

```python
CREATE VIEW allLogs AS
SELECT time::date, COUNT(*) AS logs
FROM log
GROUP BY time::date
ORDER BY time::date;
```
#2 

```python
CREATE VIEW errLogs AS
SELECT time::date, COUNT(*) AS errs
FROM log WHERE status = '404 NOT FOUND'
GROUP BY time::date
ORDER BY time::date;
```

#3 

```python
CREATE VIEW errPercentage0
AS SELECT allLogs.logs , allLogs.time , (100.0*errLogs.errs/allLogs.logs) AS percentage
FROM allLogs, errLogs, log 
WHERE allLogs.time  = errLogs.time 
ORDER BY allLogs.time

```

