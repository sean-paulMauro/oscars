from app import app

@app.route('/')
@app.route('/index')
def index():
    return "2019 Oscars Prognosticators Competition!"
