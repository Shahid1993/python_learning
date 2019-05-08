# python_learning
Python Learnings and code snippets

### What is Selenium?
  > Selenium is the Python library we use for web automation. Selenium has developed an API so third-party authors can develop webdrivers to the communication to browsers.

### Web Scraping :
  > web scraping allows you to automatically grab web content through Python.

#### [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)

#### [Package installation using pip without using cache](https://stackoverflow.com/questions/9510474/removing-pips-cache)
```shell
pip --no-cache-dir install scipy
```

#### [Upgrading Selenium version](https://stackoverflow.com/questions/43723061/selenium-is-giving-keyerror-sessionid)
```shell
pip install -U selenium
```

#### [How to add a directory to the PATH?](https://askubuntu.com/questions/60218/how-to-add-a-directory-to-the-path)
```shell
export PATH="/path/to/dir:$PATH"
```


#### [Selenium with Firefox](https://askubuntu.com/questions/851401/where-to-find-geckodriver-needed-by-selenium-python-package)
The testing machine should have selenium V. 3.0.2, firefox V. 51.0.1 (Latest version) and geckodriver v. 0.24. If you are using linux please do the following steps:
```bash
apt-get update
apt-get install firefox
pip3 install selenium==3.0.2
wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux32.tar.gz -O /tmp/geckodriver.tar.gz && tar -C /opt -xzf /tmp/geckodriver.tar.gz && chmod 755 /opt/geckodriver && ln -fs /opt/geckodriver /home/codemantra/Programs/geckodriver && ln -fs /opt/geckodriver /home/codemantra/Programs/geckodriver
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

#### [Mozilla geckodriver](https://github.com/mozilla/geckodriver/releases/tag/v0.24.0)>

#### [Selenium with Python ::: Documentation](https://selenium-python.readthedocs.io/index.html)

#### [Replacing empty csv column values with a zero](https://stackoverflow.com/questions/2862709/replacing-empty-csv-column-values-with-a-zero)
```python
for row in reader:
    for i, x in enumerate(row):
                if len(x)< 1:
                         x = row[i] = 0
                print x
```
#### [Logging with 'loguru'](https://github.com/Delgan/loguru) : 
This is a really awesome package I regularly use in my projects. It describes itself as “a library which aims to bring enjoyable logging in Python”. This package just lets you easily configure your logs out of the box.

# Resources :
- [How I used Python to analyze Game of Thrones](https://medium.freecodecamp.org/how-i-used-python-to-analyze-game-of-thrones-503a96028ce6)
- [Monitor folder and run command if there is a file there?](https://askubuntu.com/questions/893019/monitor-folder-and-run-command-if-there-is-a-file-there) 
- [10 External Python packages you are going to love](https://medium.freecodecamp.org/these-python-packages-will-help-accelerate-your-development-process-d4b3f170b1ea)
-

