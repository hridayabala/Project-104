import csv

#Weight is in pounds.

with open('data.csv', newline = '') as f:
    reader = csv.reader(f)

    file_data = list(reader)

file_data.pop(0)

newdata = []

for i in range(len(file_data)):
    weight = file_data[i][2]

    newdata.append(float(weight))

newlength = len(newdata)

sum = 0

for n in newdata:
    sum += n

mean = sum/newlength

print('The mean/average is : ' + str(mean))