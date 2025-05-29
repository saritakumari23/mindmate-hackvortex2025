from flask import Flask, render_template, request
from sentiment import analyze_sentiment

app = Flask(__name__)

checkins = []
journals = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/checkin', methods=['GET', 'POST'])
def checkin():
    if request.method == 'POST':
        mood = request.form['mood']
        note = request.form['note']
        checkins.append({'mood': mood, 'note': note})
        return render_template('checkin.html', success=True)
    return render_template('checkin.html')

@app.route('/journal', methods=['GET', 'POST'])
def journal():
    if request.method == 'POST':
        entry = request.form['entry']
        result = analyze_sentiment(entry)
        journals.append({'entry': entry, 'result': result})
        return render_template('journal.html', result=result)
    return render_template('journal.html')

@app.route('/insights')
def insights():
    return render_template('insights.html', checkins=checkins, journals=journals)

if __name__ == '__main__':
    app.run(debug=True)
