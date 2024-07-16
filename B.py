from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
    return 'BOT IS SERVING YOU'

def run():
    app.run(host='127.0.0.0', port=8010)

def b():
    server = Thread(target=run)
    server.start()
