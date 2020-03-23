# Stock-price-scraper-for-SQL
This is a simple python script to scrape stock prices off NASDAQ API and feed it to MySQL. I have spent the past 2 weeks pondering on what beginner project I should do to apply my SQL knowledge and where do I even obtain the data from? I spent some time researching and found a few option. I can import a csv file into SQLite table using SQLite3 or [DB browser for SQLite](https://sqlitebrowser.org/) or scrape the data off a webpage and feed it into MySQL. I decided to take up the challenge to extract the data myself since that is a great way for me to practise on my python skill. **Do note that I am scrapping stock prices per minute and not per day.**

## Set up 
### Dependencies 
- Python 3.8x
- python-dateutil 2.8.1 or newer
- ujson 1.35 or newer
- urllib3 1.25.8 or newer
- mysql-connector-python 8.0.18 or newer
- MySQL 8.0.19 or newer
- Internet connection

### Installing dependencies 
- **Python**: You can install Python using [Anaconda](https://www.anaconda.com/distribution/). It is the easiest way to install python and it comes with a good amount of data science packages.
- **MySQL**: I used [MySQL Community server](https://dev.mysql.com/downloads/mysql/). Please remember your password as it will need to use it everytime you log into the server. 
- **python-dateutil**,**ujson**,**mysql-connector-python**,**urllib3** can be installed using [pip](https://pypi.org/project/pip/).  
```py
$ pip install mysql-connector-python
```
or conda
```py
conda install -c anaconda mysql-connector-python
```
### What to do before running code
- Log in using:
```sql
mysql -u root -p
```
- Create a database call stock
```sql
CREATE DATABASE stock;
```
- Select database
```sql
USE stock;
```
- Create a table on your database with the same name as the stock symbol. I am using AMD for this example.
```sql
CREATE TABLE amd
  (
   datetime DATETIME,
   price FLOAT,
   created_at TIMESTAMP default now()
  );
```

### How to check if your code works
- Using SELECT * from amd
```sql
SELECT * from amd
```
 * You should able to see 3 columns of data (datetime, price and created_at)


### Licensing 
This scraper is licensed under the MIT license. You can check the information inside the LICENSE file. To make it short, I wanted it to be free and open, so that anyone can contribute to it.
