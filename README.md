# python_learning
Python Learnings and code snippets

### [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)

### [Package installation using pip without using cache](https://stackoverflow.com/questions/9510474/removing-pips-cache)
```shell
pip --no-cache-dir install scipy
```


### [Selenium with Firefox]()
The testing machine should have selenium V. 3.0.2, firefox V. 51.0.1 (Latest version) and geckodriver v. 0.14. If you are using linux please do the following steps:
```bash
apt-get update
apt-get install firefox
pip3 install selenium==3.0.2
wget https://github.com/mozilla/geckodriver/releases/download/v0.14.0/geckodriver-v0.14.0-linux64.tar.gz -O /tmp/geckodriver.tar.gz && tar -C /opt -xzf /tmp/geckodriver.tar.gz && chmod 755 /opt/geckodriver && ln -fs /opt/geckodriver /usr/bin/geckodriver && ln -fs /opt/geckodriver /usr/local/bin/geckodriver
```
To make sure that every thing is going well, check versions for all of them and make sure that its matching.

Here is an example to run
```bash
from selenium import webdriver
driver = webdriver.Firefox()
driver.get('http://google.com')
print driver.title
driver.quit()
```
