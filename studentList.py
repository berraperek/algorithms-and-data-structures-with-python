"""
Problem:
You are given two text files. One (studentList.txt) includes all student IDs that have already registered for the course
CENG888. The other file (studentListGroup.txt) contains the group id and group members (student ids in the group).
You are to do the following tasks in the programming question:
  • You are to print the students who haven’t joined a group.
  • You are expected to print the students (who already have a group but are not registered for the course) and
    discard those students from the groups.
  • The groups are expected to consist of exactly five people. Your task here is to list the groups that have fewer
    people than five. Then, you should randomly assign the students (who haven’t joined a group) to a group.
"""

with open("studentList.txt", 'r') as f1, open("studentListGroup.txt", 'r') as f2:
    student_list_txt = f1.read()
    studentList = student_list_txt.split("\n")    # migrate "studentList.txt" file to list
    studentListGroup = {}
    for line in f2.readlines():
        line = ''.join(line.splitlines())    # remove \n for each line
        key, values = line.split(":")
        studentListGroup[key] = values.strip().split(",")   # migrate "studentListGroup.txt" file to dictionary

    values = list(studentListGroup.values())
    single_list = []
    for each_group in values:
        single_list += each_group           # adding values of dictionary to single list

    not_joined_group = []
    for i in studentList:
        if i not in single_list:
            not_joined_group.append(i)

    print(not_joined_group)            # print the students who haven't joined a group

    not_registered_course = []
    for j in single_list:
        if j not in studentList:
            not_registered_course.append(j)

    print(not_registered_course)     # print the students who already have a group but are not registered for the course

    for val in studentListGroup.values():
        for element in not_registered_course:
            if element in val:
                val.remove(element)      # discard students who not registered for the course from the groups

    less_than_five = []
    for val in studentListGroup.values():
        if len(val) != 5:
            less_than_five.append(val)

    print(less_than_five)           # print the groups that have fewer people than five

    import random
    for group in less_than_five:
        while len(group) < 5:
            random_student = random.choice(not_joined_group)
            group.append(random_student)                     # randomly assigns the student who haven't joined a group
            not_joined_group.remove(random_student)          # to a group that has fewer people than five

























