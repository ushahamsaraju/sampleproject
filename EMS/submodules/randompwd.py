import string
import random
def id_generator():
    size=6
    chars=string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for x in range(size))
id_generator()
def get_emp_details(index):
    data = []
    with open("employee.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            data.append(line.split("\t")[index])
    return data
def get_Dept_details(index):
    data = []
    with open("department.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            data.append(line.split("\t")[index])
    return data
