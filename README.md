# Exporting stock prices to SQL
This is a simple python script to that extract data from a python package called yfinance and feed it to MySQL. The initial script that I have created was able to scrape data from NASDAQ API but it is no longer available. Hence, I have fall back on using the yfinance package to export stock data into my database.

## Set up 
### Dependencies 
PyMySQL==1.0.2
pandas==1.0.5
SQLAlchemy==1.3.17
yfinance==0.1.55


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

- Edit the config file
  - You will need to change the details to your own. This is an essential step to prevent the disclosure of your server details.


### Licensing 
This scraper is licensed under the GPL license. You can check the information inside the LICENSE file. To make it short, I wanted it to be free and open, so that anyone can contribute to it.
