from flask import Flask, render_template
from mostcited import most_cited
from mostrecent import most_recent
from authors import authorList
app = Flask(__name__)

@app.route("/")
def mostrecent():
    return render_template('index.html', most_recent = most_recent[:10])

@app.route("/mostcited/")
def mostcited():
    return render_template('mostcited.html', most_cited = most_cited[:10])

@app.route("/author/")
def author():
    return render_template('author.html', authors = authorList)

@app.route("/search/", methods=['GET', 'POST'])
def search():
    return render_template('search.html')

if app == '__main__':
    app.run(debug=True)