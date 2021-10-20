import feedparser

from flask import Flask

from flask import render_template

app = Flask(__name__)

RSS_FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
            'f24': 'https://www.france24.com/fr/rss',
            'cnn': 'http://rss.cnn.com/rss/edition.rss',
            'fox': 'http://feeds.foxnews.com/foxnews/latest',
            'ir': 'https://www.inter-reseaux.org/feed/',
            'nyt': 'https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml'
            }

@app.route("/")
@app.route("/<publication>")
# def bbc():
#     return get_news('bbc')

# @app.route("/cnn")
# def cnn():
#     return get_news('cnn')

# @app.route("/fox")
# def fox():
#     return get_news('fox')

# @app.route("/f24")
# def f24():
#     return get_news('f24')

def get_news(publication="f24"):
    feed = feedparser.parse(RSS_FEEDS[publication])
    # first_article = feed['entries'][0]
    return render_template("index.html", articles=feed['entries'])


# """<html>
#                 <body>
#                     <h1>Headlines </h1>
#                     <b>{0}</b> </ br>
#                     <i>{1}</i> </ br>
#                     <p>{2}</p> </ br>
#                 </body>
#             </html>""".format(first_article.get("title"), first_article.get("published"), first_article.get("summary"))
    

if __name__ == '__main__' : 
    app.run(port=3000, debug=True)