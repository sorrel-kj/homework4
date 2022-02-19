# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 13:41:07 2022

@author: 12166
"""
#open file to read data and file to write formatted data
input_file=open('weather_data.txt', 'r')
output_file=open('readable_weather.txt', 'w')

#two dictionaries
#one that will use daytime temp as keys
#one that will use nighttime temp as keys
#period_day={}
#period_night={}
#high=[]
#low=[]

#for loop reads data into one of the two dictionaries
#for line in input_file:
    #line.strip().split('something') (need to figure out how to split this stuff)
    #if "night" in [line[0]] and [line[0]] not in period_night.keys():
        #period_night[line[0]]=[line[2]]
    #if "night" in [line[0]] and [line[0]] in period_night.keys():
        #period_night[line[0]].append(line[2])
    #if "night" not in [line[0]] and [line[0]] not in period_day.keys():
        #period_days[line[0]]=[line[2]]
    #if "night" not in [line[0]] and [line[0]] in period_day.keys():
        #period_day[line[0]].append(line[2]])
    #if "high" in line[2] and line[2] not in high:
        #high.append(line[2])
    #if "low" in line[2] and line[2] not in low:
        #low.append(line[2])
    
    
#find the date with the highest temperature
#max_period=max(period_day, key=period_day.get)
#find the highest temperature
#max_temp=max(period_day.values())

#same processes but for the lowest temperature!
#min_period=min(period_night, key=period_night.get)
#min_temp=min(period_night.values())

#average day-time temp
#avg_day=(sum(high)/len(high))

#average night-time temp
#avg_night=(sum(low)/len(low))

#write all our data to the output file!!
#output_file.write('Highest temperature: '+max_temp+'\n')
#output_file.write('Hottest period: '+max_period+'\n\n')
#output_file.write('Average temperature in the daytime: '+avg_day+'\n')
#output_file.write('Average temperature in the nighttime: '+avg_night+'\n)

#close all our files :D
#input_file.close()
#output_file.close()

