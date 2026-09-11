import os
import redis
import psycopg2
from flask import Flask

app = Flask(__name__)
r = redis.from_url(os.getenv('REDIS_URL', 'redis://cache:6379'))

@app.route('/')
def hello():
    count = r.incr('hits')
    return f'Hello from Flask! Visits: {count}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
