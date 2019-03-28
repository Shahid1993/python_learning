# run.py

from eve import Eve
import pdb
from worker import populate_dotmark

def after_insert(resource, items):
	print "after insert"
	for item in items:
		url = item['url']
		object_id = item['_id']
		print url
		print object_id
		populate_dotmark(object_id, url)
		

def before_insert(resource_name, items):
	print "Something is going to be inserted"

app = Eve()

app.on_insert += before_insert
app.on_inserted += after_insert

if __name__ == '__main__':
    app.run( host = '0.0.0.0', port = 5000, debug = True)

# worker.py
from flask import Flask
from celery import Celery
import urllib2
from BeautifulSoup import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client.eve

def make_celery(app):
    celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    TaskBase = celery.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery

flask_app = Flask(__name__)
flask_app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379',
    CELERY_RESULT_BACKEND='redis://localhost:6379'
)
celery = make_celery(flask_app)

@celery.task()
def populate_dotmark(object_id, url):
	print "processing %s" % url
	soup = BeautifulSoup(urllib2.urlopen(url))
	title = soup.title.string
	updates = {'title': title}
	db.dotmarks.update({'_id': object_id}, {"$set": updates}, upsert=False)
return 1
