from connector import Connector

class Employees:

    @staticmethod
    def get_all():
        query = "SELECT * FROM employees"
        try:
            Connector.cursor.execute(query)
            result = Connector.cursor.fetchall()
            return result
        except Exception as e:
            print("Error retrieving employees:", e)
            return [] 

    @staticmethod
    def add_employee(emp_id, lname, fname, mname):
        query = "INSERT INTO employees VALUES (%s, %s, %s, %s)"
        try:
            Connector.cursor.execute(query, (emp_id, lname, fname, mname))
            Connector.db.commit()
            return True
        except Exception as e:
            print("Error adding employee:", e)
            return False

    @staticmethod
    def update_employee(emp_id, lname, fname, mname):
        query = "UPDATE employees SET lname=%s, fname=%s, mname=%s WHERE emp_id=%s"
        try:
            Connector.cursor.execute(query, (lname, fname, mname, emp_id))
            Connector.db.commit()
            return True
        except Exception as e:
            print("Error updating employee:", e)
            return False

    @staticmethod
    def get_employee(emp_id):
        query = "SELECT * FROM employees WHERE emp_id = %s"
        try:
            Connector.cursor.execute(query, (emp_id,))
            employee = Connector.cursor.fetchone()
            return employee
        except Exception as e:
            print("Error retrieving employee:", e)
            return None

    @staticmethod
    def delete_employee(emp_id):
        query = "DELETE FROM employees WHERE emp_id = %s"
        try:
            Connector.cursor.execute(query, (emp_id,))
            Connector.db.commit()
            return True
        except Exception as e:
            print("Error deleting employee:", e)
            return False
