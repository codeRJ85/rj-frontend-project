from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Bangaluru,India',
        'salary': 'Rs. 1,00,000'
    },
    {
        'id': 2,
        'title': 'Video Editor',
        'location': 'Delhi,India',
        'salary': 'Rs. 5,00,000'
    },
    {
        'id': 3,
        'title': 'Data Scientist',
        'location': 'Kolkata,India',
        'salary': 'Rs. 3,00,000'
    },
    {
        'id': 4,
        'title': 'Front-end Developer',
        'location': 'Bangaluru,India',
        'salary': 'Rs. 4,00,000'
    },
    {
        'id': 5,
        'title': 'Backend Developer',
        'location': 'Chennai,India',
        'salary': 'Rs. 6,00,000'
    }
]

@app.route("/")
def hello_world():
    return render_template('home.html', jobs=JOBS, company_name='Rcareer')

@app.route("/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
