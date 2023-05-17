from flask import Flask, render_template, jsonify
from flask_mysqldb import MySQL
import database

app = database.app

mysql = MySQL(database.app)

JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'Bengaluru, India',
  'salary': 'Rs. 10,00,000'
}, {
  'id': 2,
  'title': 'Data Scientist',
  'location': 'Delhi, India',
  'salary': 'Rs. 15,00,000'
}, {
  'id': 3,
  'title': 'Frontend Engineer',
  'location': 'Remote'
}, {
  'id': 4,
  'title': 'Backend Engineer',
  'location': 'San Francisco, USA',
  'salary': '$150,000'
}]


@app.route('/')
def hello_workd():
  cur = mysql.connection.cursor()
  cur.execute('SELECT * FROM jobs')
  jobs = cur.fetchall()
  cur.close()

  result = []

  for job in jobs:
    result.append({
      'id': job[0],
      'title': job[1],
      'location': job[2],
      'salary': job[3],
      'currency': job[4],
      'responsibilities': job[5],
      'requirements': job[6]
    })
  return render_template('home.html', jobs=result)


# @app.route('/api/jobs')
# def jobs():
#   cur = mysql.connection.cursor()
#   cur.execute('SELECT * FROM jobs')
#   jobs = cur.fetchall()
#   cur.close()
#
#   result = []
#
#   for job in jobs:
#     result.append({
#       'id': job[0],
#       'title': job[1],
#       'location': job[2],
#       'salary': job[3],
#       'currency': job[4],
#       'responsibilities': job[5],
#       'requirements': job[6]
#     })
#
#   return jsonify(result)

# @app.route('/insertrecord')
# def insert_job():
#     cur = mysql.connection.cursor()
#     job = [{
#         'title': 'Data Scientist',
#         'location': 'New York',
#         'salary': 120000,
#         'currency': 'USD',
#         'responsibilities': 'Analyze data, develop models, and communicate insights',
#         'requirements': 'Experience with Python, SQL, and machine learning'
#     },{
#         'title': 'Data Analyst',
#         'location': 'Bengaluru',
#         'salary': 1000000,
#         'currency': 'India',
#         'responsibilities': 'Analyze data, develop models, and communicate insights',
#         'requirements': 'Experience with Python, SQL, and machine learning'
#     },{
#         'title': 'Backend Engineer',
#         'location': 'San Francisco',
#         'salary': 1000000,
#         'currency': 'USA',
#         'responsibilities': 'Analyze data, develop models, and communicate insights',
#         'requirements': 'Experience with Python, SQL, and machine learning'
#     }]
#     cur.executemany('''
#         INSERT INTO jobs (title, location, salary, currency, responsibilities, requirements)
#         VALUES (%(title)s, %(location)s, %(salary)s, %(currency)s, %(responsibilities)s, %(requirements)s)
#     ''', job)
#     mysql.connection.commit()
#     cur.close()
#     return 'Job inserted successfully!'



if __name__ == '__main__':
  app.run()
