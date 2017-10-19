# Log Analysis Project

### Project Overview
Created a reporting tool that prints out reports (in plain text) based on the data in a database. 
This reporting tool is written with Python 3.6.2 using the `psycopg2` module to connect to the database.
No views were made in the Postgresql database.

### Assignment
The reporting tool reported the following questions:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

### Running the Program
1. Install <a href="https://www.vagrantup.com/">Vagrant</a> and <a href="https://www.virtualbox.org/wiki/VirtualBox">VirtualBox</a>.
2. Clone the <a href="https://github.com/udacity/fullstack-nanodegree-vm">Udacity Vagrant</a> repository and run vagrant up in the vagrant directory.
3. Load the data in the vagrant directory using the command: psql -d news -f newsdata.sql
4. Connect to the Postgres news database with psql: psql news
5. In the psql news=> terminal, type \dt to ensure there are 3 tables (articles, authors, logs)
6. Hit Ctrl + D to exit the psql shell. 
7. Run `python log_analysis.py` in the LogAnalysis directory to see the top articles, authors, and dates with more than 1% errors.

### Example Output
An example output is in example.txt
