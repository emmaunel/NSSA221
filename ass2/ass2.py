import csv
import pwd, grp
from subprocess import *
import os


def makegroup(group):
    os.system("groudadd " + group)

def makeit(first, last):
    if len(first) < 1:
        user = last
    elif len(last) < 1:
        user = first
    else:
        user = first[0] + last

    return user


def adduser(first, last, group, department):
    username = makeit(first, last)
    print(username)
    # gid = groudid(group)
    # print(gid)


with open('user.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    next(csvReader)
    for row in csvReader:
        id = row[0]
        lastname = row[1]
        firstname = row[2]
        office = row[3]
        phone = row[4]
        department = row[5]
        group = row[6]

        # print(firstname)
        if not firstname or not lastname:
            print("Error in this line ", row)
            continue

        adduser(firstname, lastname, group, department)
