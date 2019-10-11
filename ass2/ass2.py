import csv
import os
import random


def makeit(first, last):
    first = first.replace("\'", '')
    last = last.replace("\'", '')
    if len(first) < 1:
        user = last
    elif len(last) < 1:
        user = first
    else:
        user = first[0] + last + str(random.randint(1,20))

    return user.lower()


def adduser(first, last, group, department):
    username = makeit(first, last)

    os.system("groupadd " + group + " > /dev/null 2>&1")

    shell = "/bin/bash"
    directory = "/home/" + department + "/" + username
    os.system("mkdir -p " + directory)
    comment = firstname + " " + lastname

    # Create user
    os.system("useradd -m -d " + directory + " -s " + shell + " -g " + group + " -c \"" + comment + "\" " + username + " > /dev/null 2>&1")
    print("useradd -m -d " + directory + " -s " + shell + " -g " + group + " -c \"" + comment + "\" " + username)

    # change user password
    os.system("echo " + username[::-1] + " | passwd " + username + " --stdin")

    # expire user password
    os.system("passwd -e " + username)
    print("\n")


with open('user.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    next(csvReader)
    error = []
    for row in csvReader:
        id = row[0]
        lastname = row[1]
        firstname = row[2]
        office = row[3]
        phone = row[4]
        department = row[5]
        group = row[6]

        if not firstname or not lastname or not group or not department:
            # print("Error in this line ", row)
            error.append(id)
            continue

        adduser(firstname, lastname, group, department)
    for i in error:
	print("BAD RECORD: EmployeeID= " + i)
