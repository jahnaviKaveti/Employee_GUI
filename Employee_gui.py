
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import os
import csv

EMPLOYEE_FILE = "employee.csv"

# Ensure employee file exists with headers
if not os.path.exists(EMPLOYEE_FILE):
    with open(EMPLOYEE_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Name", "Position", "Salary"])

def load_employees():
    with open(EMPLOYEE_FILE, newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)

def save_employees(employees):
    with open(EMPLOYEE_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["ID", "Name", "Position", "Salary"])
        writer.writeheader()
        writer.writerows(employees)

def add_employee():
    emp_id = simpledialog.askstring("Add Employee", "Enter Employee ID:")
    if not emp_id:
        return
    employees = load_employees()
    for emp in employees:
        if emp["ID"] == emp_id:
            messagebox.showerror("Error", "Employee ID already exists!")
            return
    name = simpledialog.askstring("Add Employee", "Enter Name:")
    position = simpledialog.askstring("Add Employee", "Enter Position:")
    salary = simpledialog.askstring("Add Employee", "Enter Salary:")
    employees.append({"ID": emp_id, "Name": name, "Position": position, "Salary": salary})
    save_employees(employees)
    messagebox.showinfo("Success", "Employee added successfully!")
    view_employees()

def view_employees():
    for i in tree.get_children():
        tree.delete(i)
    employees = load_employees()
    for emp in employees:
        tree.insert("", "end", values=(emp["ID"], emp["Name"], emp["Position"], emp["Salary"]))

def search_employee():
    emp_id = simpledialog.askstring("Search Employee", "Enter Employee ID:")
    employees = load_employees()
    for emp in employees:
        if emp["ID"] == emp_id:
            messagebox.showinfo("Employee Found", f"ID: {emp['ID']}\nName: {emp['Name']}\nPosition: {emp['Position']}\nSalary: {emp['Salary']}")
            return
    messagebox.showerror("Not Found", "Employee ID not found.")

def update_employee():
    emp_id = simpledialog.askstring("Update Employee", "Enter Employee ID to update:")
    employees = load_employees()
    for emp in employees:
        if emp["ID"] == emp_id:
            emp["Name"] = simpledialog.askstring("Update Employee", "Enter New Name:", initialvalue=emp["Name"])
            emp["Position"] = simpledialog.askstring("Update Employee", "Enter New Position:", initialvalue=emp["Position"])
            emp["Salary"] = simpledialog.askstring("Update Employee", "Enter New Salary:", initialvalue=emp["Salary"])
            save_employees(employees)
            messagebox.showinfo("Success", "Employee updated successfully!")
            view_employees()
            return
    messagebox.showerror("Not Found", "Employee ID not found.")

def delete_employee():
    emp_id = simpledialog.askstring("Delete Employee", "Enter Employee ID to delete:")
    employees = load_employees()
    updated_employees = [emp for emp in employees if emp["ID"] != emp_id]
    if len(updated_employees) != len(employees):
        save_employees(updated_employees)
        messagebox.showinfo("Success", "Employee deleted successfully!")
        view_employees()
    else:
        messagebox.showerror("Not Found", "Employee ID not found.")

# GUI setup
root = tk.Tk()
root.title("Employee Management System")
root.geometry("600x400")

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Employee Management System", font=("Arial", 18)).pack()

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Add", width=12, command=add_employee).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="View", width=12, command=view_employees).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Search", width=12, command=search_employee).grid(row=0, column=2, padx=5)
tk.Button(button_frame, text="Update", width=12, command=update_employee).grid(row=0, column=3, padx=5)
tk.Button(button_frame, text="Delete", width=12, command=delete_employee).grid(row=0, column=4, padx=5)

tree = ttk.Treeview(root, columns=("ID", "Name", "Position", "Salary"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Name", text="Name")
tree.heading("Position", text="Position")
tree.heading("Salary", text="Salary")
tree.pack(pady=10, fill=tk.BOTH, expand=True)

view_employees()

root.mainloop()
