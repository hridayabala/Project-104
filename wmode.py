from collections import Counter
import csv

#Weight is in pounds.

with open('data.csv', newline = '')as f:
    reader = csv.reader(f)

    file_data = list(reader)

file_data.pop(0)

newdata = []

for i in range(len(file_data)):
    weight = file_data[i][2]

    newdata.append(weight)

data = Counter(newdata)

modedataforrange = {
    '110 - 120' : 0,
    '120 - 130' : 0,
    '130 - 140' : 0,
    '140 - 150' : 0

}

for weightdata, occurance in data.items():
    if 110 < float(weightdata) < 120:
        modedataforrange['110 - 120'] += occurance

    elif 120 < float(weightdata) < 130:
        modedataforrange['120 - 130'] += occurance
    
    elif 130 < float(weightdata) < 140:
        modedataforrange['130 - 140'] += occurance
    
    elif 140 < float(weightdata) < 150:
        modedataforrange['140 - 150'] += occurance

moderange = 0
modeoccurance = 0

for range, occurance in modedataforrange.items():
    if occurance > modeoccurance:
        moderange, modeoccurance = [int(range.split('-')[0]), int(range.split('-')[1])], occurance

mode = float((moderange[0] + moderange[1])/2)

print('The mode is : ' + str(mode))
