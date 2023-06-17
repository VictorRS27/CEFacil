from flask import Flask, render_template
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)

def minha_funcao():
    print('Tudo certo')

scheduler = BackgroundScheduler(daemon=True)
scheduler.add_job(minha_funcao, 'interval', minutes=10)
scheduler.start()

@app.route('/')
def home():
    return render_template('./site/home.html')

@app.route('/cefer')
def cefer():
    return render_template('./site/cefer.html')

@app.route('/about')
def about():
    return render_template('./site/about.html')
if __name__ == '__main__':
    app.run()
