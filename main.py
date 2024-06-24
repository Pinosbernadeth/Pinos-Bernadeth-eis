from flask import Flask, render_template, request, redirect, session, url_for
from users import Users
from employees import Employees

app = Flask(__name__)
app.secret_key = "secret"

# Login route
@app.route('/')
def login():
    return render_template('login.html')

# Check user credentials
@app.route('/check-user', methods=['POST'])
def check_user():
    username = request.form["username"]
    password = request.form["password"]

    result = Users.check_user(username, password)

    if result:
        return redirect('/employee-list')
    else:
        return render_template('login.html', message="Invalid credentials. Please try again.")

# Display employee list
@app.route('/employee-list')
def employee_list():
    employees = Employees.get_all()
    message = session.pop("message", "")
    return render_template('employee_list.html', employees=employees, message=message)

# Display add employee form
@app.route('/add-form')
def add_form():
    return render_template('add_employee.html')

# Add new employee
@app.route('/add-employee', methods=["POST"])
def add_employee():
    emp_id = request.form["emp_id"]
    lname = request.form["lname"]
    fname = request.form["fname"]
    mname = request.form["mname"]

    success = Employees.add_employee(emp_id, lname, fname, mname)

    if success:
        session["message"] = "Successfully added employee"
    else:
        session["message"] = "Failed to add employee"

    return redirect('/employee-list')

# Display update employee form and handle update
@app.route('/update-employee/<emp_id>', methods=['GET', 'POST'])
def update_employee(emp_id):
    if request.method == 'POST':
        lname = request.form['lname']
        fname = request.form['fname']
        mname = request.form['mname']

        success = Employees.update_employee(emp_id, lname, fname, mname)

        if success:
            session["message"] = "Successfully updated employee"
        else:
            session["message"] = "Failed to update employee"

        return redirect('/employee-list')
    else:
        employee = Employees.get_employee(emp_id)
        if employee:
            return render_template('update_employee.html', employee=employee)
        else:
            session["message"] = f"Employee with ID {emp_id} not found."
            return redirect('/employee-list')

# Delete employee
@app.route('/delete-employee/<emp_id>', methods=["POST"])
def delete_employee(emp_id):
    success = Employees.delete_employee(emp_id)

    if success:
        session["message"] = "Successfully deleted employee"
    else:
        session["message"] = "Failed to delete employee"

    return redirect(url_for('employee_list'))

if __name__ == '__main__':
    app.run(debug=True)
