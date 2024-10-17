from flask import Flask, request, render_template, jsonify
from services.news_fetcher import get_trending_news
from models.generator import generate_content_ideas

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        field = request.form['field']
        news_data = get_trending_news(field)
        ideas = generate_content_ideas(news_data)
        return jsonify({'ideas': ideas})
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
