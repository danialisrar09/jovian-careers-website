from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Remote',
        'Salary': 'Rs. 1,000,000',
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Karachi, Pakistan',
        'Salary': 'Rs. 1,500,000',
    },
    {
        'id': 3,
        'title': 'Data Engineer',
        'location': 'Remote',
        'company': 'Jovian',
        'Salary': 'Rs. 900,000',
    },
    {
        'id': 4,
        'title': 'Software Engineer',
        'location': 'Lahore, Pakistan',
        'Salary': 'Rs. 800,000',
    }
]
@app.route("/")
def hello_jovian():
    return render_template('home.html', jobs = JOBS, company = "Jovian")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)