import feedparser

from flask import Flask

from flask import render_template

from flask import request


app = Flask(__name__)

RSS_FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
            'f24': 'https://www.france24.com/fr/rss',
            'cnn': 'http://rss.cnn.com/rss/edition.rss',
            'fox': 'http://feeds.foxnews.com/foxnews/latest',
            'ir': 'https://www.inter-reseaux.org/feed/',
            'nyt': 'https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml'
            }

@app.route("/")
def get_news():
    query = request.args.get("publication")
    if not query or query.lower() not in RSS_FEEDS : 
        publication = "bbc"
    else:
        publication = query.lower()
    feed = feedparser.parse(RSS_FEEDS[publication])
    # first_article = feed['entries'][0]
    return render_template("index.html", articles=feed['entries'])

if __name__ == '__main__' : 
    app.run(port=3000, debug=True)