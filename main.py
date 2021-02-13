from commentScraper import search_comments, scrape
from flask import Flask, render_template, request, redirect


app = Flask("SuperScrapper")
db = {}


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/search")
def report():
    word = request.args.get("word")
    url = request.args.get("link")
    if word:
        word = word.lower()
        comments_list = db.get(url)

        if comments_list:
            selected_comments = search_comments(comments_list, word)
        else:
            all_comments = scrape(url)
            db[url] = all_comments
            selected_comments = search_comments(all_comments, word)

    else:
        return redirect("/")
    return render_template(
            'result.html',
            word=word,
            resultNumber=len(selected_comments),
            comments=selected_comments
            )


app.run(host="127.0.0.1")