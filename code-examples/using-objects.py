# Perform operations on the values of objects (dicts) in an array 

myObj = [
    {'name': 'Alice', 'major': 'cs', 'gpa': 3.5},
    {'name': 'Bob', 'major': 'ee', 'gpa': 3.9},
    {'name': 'Craig', 'major': 'me', 'gpa': 3.2},
    {'name': 'Daphne', 'major': 'ee', 'gpa': 3.8},
    {'name': 'Edward', 'major': 'me', 'gpa': 4.0},
    {'name': 'Fred', 'major': 'cs', 'gpa': 2.8},
    {'name': 'Gertrude', 'major': 'cs', 'gpa': 3.4},
    {'name': 'Harry', 'major': 'ee', 'gpa': 3.2},
    {'name': 'Isabel', 'major': 'cs', 'gpa': 3.0},
    {'name': 'Justin', 'major': 'me', 'gpa': 2.5},
    {'name': 'Kaden', 'major': 'cs', 'gpa': 1.9}
]

# create dicts to get sum of gpa's for each major, and the amount of people in each major
majorGpaSums = {}
majorCount = {}

# determine which majors are present 
for obj in myObj:
    majorGpaSums[obj['major']] = 0
    majorCount[obj['major']] = 0

# get sum of gpa's
for obj in myObj:
    majorGpaSums[obj['major']] += obj['gpa'] 
    majorCount[obj['major']] += 1

# output info found 
for major in majorGpaSums:
    print(major, ': ', majorCount[major], ' students, ', round(majorGpaSums[major]/majorCount[major], 2), ' average gpa', sep='')
