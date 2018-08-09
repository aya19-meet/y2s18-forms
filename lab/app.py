from databases import *
from flask import Flask, render_template, url_for, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', students=query_all())

@app.route('/student/<int:student_id>')
def display_student(student_id):
    return render_template('student.html', student=query_by_id(student_id))

@app.route('/add', methods=['GET', 'POST'])
def add_student_route():
	if request.method == 'GET':
		return render_template('add.html')
	else:
		add_student(request.form['student_name'],
			request.form['student_year'], False)
		return render_template('add.html')

@app.route('/delete/<int:student_id>', methods=['GET','POST'])
def delete_student_id(student_id):
	delete_by_id(student_id)
	return render_template('delete.html', student_id = student_id)

@app.route('/edit/<int:student_id>', methods=['GET','POST'])
def edit_lab_status(student_id):
	if request.method == 'GET':
		student = query_by_id(student_id)
		return render_template('edit.html', student = student)
	else:
		student = query_by_id(student_id)
		lab = request.form['lab_status']
		if(lab == "Finished"):
			student.finished_lab = True
		else:
			student.finished_lab = False
		session.commit()
		return render_template('edit.html', student = student)


app.run(debug=True)
