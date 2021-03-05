# Part. 1

#=======================================

# Import module

#  csv -- fileIO operation

import csv

#=======================================


# Part. 2

#=======================================

# Read cwb weather data

cwb_filename = '108061228.csv'

data = []

header = []

maximum = [-999] * 5

with open(cwb_filename) as csvfile:

    mycsv = csv.DictReader(csvfile)

    header = mycsv.fieldnames

    for row in mycsv:

        data.append(row)
      
        if(row['WDSD'] == '-99.000' or row['WDSD'] == '-999.000'):
            row['WDSD'] = ''
        if(row['station_id'] == 'C0A880'):
            if(row['WDSD'] != ''):
                if(float(row['WDSD']) > maximum[0]):
                    maximum[0] = float(row['WDSD'])
        if(row['station_id'] == 'C0F9A0'):
            if(row['WDSD'] != ''):
                if(float(row['WDSD']) > maximum[1]):
                    maximum[1] = float(row['WDSD'])
        if(row['station_id'] == 'C0G640'):
            if(row['WDSD'] != ''):
                if(float(row['WDSD']) > maximum[2]):
                    maximum[2] = float(row['WDSD'])
        if(row['station_id'] == 'C0R190'):
            if(row['WDSD'] != ''):
                if(float(row['WDSD']) > maximum[3]):
                    maximum[3] = float(row['WDSD'])
        if(row['station_id'] == 'C0X260'):
            if(row['WDSD'] != ''):
                if(float(row['WDSD']) > maximum[4]):
                    maximum[4] = float(row['WDSD'])

    
    
        
    

#=======================================


# Part. 3

#=======================================

# Analyze data depend on your group and store it to target_data like:

# Retrive all data points which station id is "C0X260" as a list.

# target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))


# Retrive ten data points from the beginning.

target_data = data[:10]

def Output(name, Max):
    print("['", end = '')
    print(name, end = '')
    print("', ", end = '')
    if(Max == -999):
        print("'None'", end = '')
    else:
        print(Max, end = '')
    print("]", end = '')

#=======================================


# Part. 4

#=======================================

# Print result

#print(target_data)

print('[', end = '')
Output('C0A880', maximum[0])
print(', ', end = '')
Output('C0F9A0', maximum[1])
print(', ', end = '')
Output('C0G640', maximum[2])
print(', ', end = '')
Output('C0R190', maximum[3])
print(', ', end = '')
Output('C0X260', maximum[4])
print(']')

#========================================