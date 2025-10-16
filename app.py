from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('jobs.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            company TEXT NOT NULL,
            description TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/', methods=['GET', 'POST'])
def index():
    conn = sqlite3.connect('jobs.db')
    c = conn.cursor()

    if request.method == 'POST':
        title = request.form['title']
        company = request.form['company']
        description = request.form['description']
        c.execute('INSERT INTO jobs (title, company, description) VALUES (?, ?, ?)',
                  (title, company, description))
        conn.commit()
        conn.close()
        return redirect('/')

    c.execute('SELECT * FROM jobs')
    jobs = c.fetchall()
    conn.close()
    return render_template('index.html', jobs=jobs)

@app.route('/delete/<int:id>')
def delete_job(id):
    conn = sqlite3.connect('jobs.db')
    c = conn.cursor()
    c.execute('DELETE FROM jobs WHERE id=?', (id,))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
