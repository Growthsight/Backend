#!/usr/bin/python
import sys
import forecastio
import datetime

''' KEY FOR THE API TO WORK'''
api_key = "c6a99c6932310919951887873b154cbb"

''' DECLARE VARIABLE WITH INITAIL VALUE TO 0'''
day_avg_temp = 0
day_sum_temp = 0
month_avg_temp = 0
month_sum_temp = 0
year_avg_temp_soyabean = 0
year_avg_temp_swheat = 0
year_avg_temp_wwheat = 0
year_avg_temp_cotton = 0
year_avg_temp_strawberry = 0
year_sum_temp_soyabean = 0
year_sum_temp_swheat = 0
year_sum_temp_wwheat = 0
year_sum_temp_cotton = 0
year_sum_temp_strawberry = 0
optimal_avg_temp_soyabean = 0
optimal_avg_temp_corn = 0
optimal_avg_temp_swheat = 0
optimal_avg_temp_wwheat = 0
optimal_avg_temp_cotton = 0
optimal_avg_temp_strawberry = 0
optimal_sum_temp_soyabean = 0
optimal_sum_temp_swheat = 0
optimal_sum_temp_wwheat = 0
optimal_sum_temp_cotton = 0
optimal_sum_temp_strawberry = 0
day_avg_hum = 0
day_sum_hum = 0
month_avg_hum = 0
month_sum_hum = 0
year_avg_hum_soyabean = 0
year_avg_hum_cotton = 0
year_avg_hum_swheat = 0
year_avg_hum_wwheat = 0
year_avg_hum_strawberry = 0
year_sum_hum_soyabean = 0
year_sum_hum_swheat = 0
year_sum_hum_wwheat = 0
year_sum_hum_cotton = 0
year_sum_hum_strawberry = 0
optimal_avg_hum_soyabean = 0
optimal_avg_hum_corn = 0
optimal_avg_hum_swheat = 0
optimal_avg_hum_wwheat = 0
optimal_avg_sum_cotton = 0
optimal_avg_sum_strawberry = 0
optimal_sum_hum_soyabean = 0
optimal_sum_hum_swheat = 0
optimal_sum_hum_wwheat = 0
optimal_sum_hum_cotton = 0
optimal_sum_hum_strawberry = 0
day_avg_precip = 0
day_sum_precip = 0
month_avg_precip = 0
month_sum_precip = 0
year_avg_precip_soyabean = 0
year_avg_precip_cotton = 0
year_avg_precip_swheat = 0
year_avg_precip_wwheat = 0
year_avg_precip_strawberry = 0
year_sum_precip_soyabean = 0
year_sum_precip_swheat = 0
year_sum_precip_wwheat = 0
year_sum_precip_cotton = 0
year_sum_precip_strawberry = 0
optimal_avg_precip_soyabean = 0
optimal_avg_precip_corn = 0
optimal_avg_precip_swheat = 0
optimal_avg_precip_wwheat = 0
optimal_avg_precip_cotton = 0
optimal_avg_precip_strawberry = 0
optimal_sum_precip_soyabean = 0
optimal_sum_precip_swheat = 0
optimal_sum_precip_wwheat = 0
optimal_sum_precip_cotton = 0
optimal_sum_precip_strawberry = 0

''' VARIABLES TO CALCULATE NUMBER OF DATA POINTS THAT DOES NOT EXIST'''
temp_error = 0
hum_error = 0
precip_error = 0
hour_error = 0;

'''LOOPING THROUGH DIFFERENT YEARS'''
for year in range(2000,2001):	
	'''LOOPING THROUGH DIFFERENT MONTHS'''
	for month in range(1,11):
		'''LOOPING THROUGH DIFFERENT DAYS'''
		for day in range(1,29):
			current_time = datetime.datetime(year,month,day)					#CALCULATE SPECIFIC DAY
			forecast = forecastio.load_forecast(api_key,sys.argv[1],sys.argv[2],time=current_time)	#API CALL FOR SPECIFIC DAY	
			byHour = forecast.hourly()								#HOURLY DATA OBJECT
			'''LOOPING THOUGH DIFFERENT HOURS'''
			for hours in range(0,24):								#24 Hour DATA
				try:			
					hour_error = hour_error + 1
					try:
						day_sum_temp = day_sum_temp + byHour.data[hours].temperature
					except AttributeError:						#EXCEPTION HANDLING IF NO DATAPOINT
						temp_error = temp_error + 1
					try:
						day_sum_hum = day_sum_hum + byHour.data[hours].humidity*100
					except AttributeError:						#EXCEPTION HANDLING IF NO DATAPOINT
						hum_error = hum_error + 1
					try:
						day_sum_precip = day_sum_precip + byHour.data[hours].precipIntensity
					except AttributeError:						#EXCEPTION HANDLING IF NO DATAPOINT
						precip_error = precip_error + 1
				except:
					hour_error = hour_error - 1
			if day_sum_temp == 0:
				day_avg_temp = 0
			else:
				day_avg_temp = day_sum_temp/(24 - temp_error)
			if day_sum_hum == 0:
				day_avg_hum = 0
			else:
				day_avg_hum = day_sum_hum/(24 - hum_error)
			if day_sum_precip == 0:
				day_avg_precip = 0
			else:
				day_avg_precip = day_sum_precip/(24 - precip_error)
			day_sum_temp = 0
			day_sum_hum = 0
			day_sum_precip = 0
			temp_error = 0
			hum_error = 0
			precip_error = 0
			hour_error = 0
			month_sum_temp = month_sum_temp + day_avg_temp
			month_sum_hum = month_sum_hum + day_avg_hum
			month_sum_precip = month_sum_precip + day_avg_precip
		if month_sum_temp == 0:
			month_avg_temp = 0
		else:
			month_avg_temp = month_sum_temp/28
		if month_sum_hum == 0:
			month_avg_hum = 0
		else:
			month_avg_hum = month_sum_hum/28
		if month_sum_precip == 0:
			month_avg_precip = 0
		else:
			month_avg_precip = month_sum_precip/28
		month_sum_temp = 0
		month_sum_hum = 0
		month_sum_precip = 0
		if month in range(1,6):
			year_sum_temp_strawberry = year_sum_temp_strawberry + month_avg_temp
			year_sum_hum_strawberry = year_sum_hum_strawberry + month_avg_hum
			year_sum_precip_strawberry = year_sum_precip_strawberry + month_avg_precip
		if month in range(3,7):
			year_sum_temp_cotton = year_sum_temp_cotton + month_avg_temp
			year_sum_hum_cotton = year_sum_hum_cotton + month_avg_hum
			year_sum_precip_cotton = year_sum_precip_cotton + month_avg_precip
		if month in range(4,7):
			year_sum_temp_soyabean = year_sum_temp_soyabean + month_avg_temp
			year_sum_hum_soyabean = year_sum_hum_soyabean + month_avg_hum
			year_sum_precip_soyabean = year_sum_precip_soyabean + month_avg_precip
		if month in range(4,6):
			year_sum_temp_swheat = year_sum_temp_swheat + month_avg_temp
			year_sum_hum_swheat = year_sum_hum_swheat + month_avg_hum
			year_sum_precip_swheat = year_sum_precip_swheat + month_avg_precip
		if month in range(8,11):
			year_sum_temp_wwheat = year_sum_temp_wwheat + month_avg_temp
			year_sum_hum_wwheat = year_sum_hum_wwheat + month_avg_hum
			year_sum_precip_wwheat = year_sum_precip_wwheat + month_avg_precip
	if year_sum_temp_strawberry == 0:
		year_avg_temp_strawberry = 0
	else:
		year_avg_temp_strawberry = year_sum_temp_strawberry/5
	if year_sum_hum_strawberry == 0:
		year_avg_hum_strawberry = 0
	else:
		year_avg_hum_strawberry = year_sum_hum_strawberry/5
	if year_sum_precip_strawberry == 0:
		year_avg_precip_strawberry = 0
	else:
		year_avg_precip_strawberry = year_sum_precip_strawberry/5
	if year_sum_temp_cotton == 0:
		year_avg_temp_cotton = 0
	else:
		year_avg_temp_cotton = year_sum_temp_cotton/4
	if year_sum_hum_cotton == 0:
		year_avg_hum_cotton = 0
	else:
		year_avg_hum_cotton = year_sum_hum_cotton/4
	if year_sum_precip_cotton == 0:
		year_avg_precip_cotton = 0
	else:
		year_avg_precip_cotton = year_sum_precip_cotton/4
	if year_sum_temp_soyabean == 0:
		year_avg_temp_soyabean = 0
	else:
		year_avg_temp_soyabean = year_sum_temp_soyabean/3
	if year_sum_hum_soyabean == 0:
		year_avg_hum_soyabean = 0
	else:
		year_avg_hum_soyabean = year_sum_hum_soyabean/3
	if year_sum_precip_soyabean == 0:
		year_avg_precip_soyabean = 0
	else:
		year_avg_precip_soyabean = year_sum_precip_soyabean/3
	if year_sum_temp_swheat == 0:
		year_avg_temp_swheat = 0
	else:
		year_avg_temp_swheat = year_sum_temp_swheat/2
	if year_sum_hum_swheat == 0:
		year_avg_hum_swheat = 0
	else:
		year_avg_hum_swheat = year_sum_hum_swheat/2
	if year_sum_precip_swheat == 0:
		year_avg_precip_swheat = 0
	else:
		year_avg_precip_swheat = year_sum_precip_swheat/2
	if year_sum_temp_wwheat == 0:
		year_avg_temp_wwheat = 0
	else:
		year_avg_temp_wwheat = year_sum_temp_wwheat/3
	if year_sum_hum_wwheat == 0:
		year_avg_hum_wwheat = 0
	else:
		year_avg_hum_wwheat = year_sum_hum_wwheat/3
	if year_sum_precip_wwheat == 0:
		year_avg_precip_wwheat = 0
	else:
		year_avg_precip_wwheat = year_sum_precip_wwheat/3
	year_sum_temp_strawberry = 0
	year_sum_hum_strawberry = 0
	year_sum_precip_strawberry = 0
	year_sum_temp_cotton = 0
	year_sum_hum_cotton = 0
	year_sum_precip_cotton = 0
	year_sum_temp_soyabean = 0
	year_sum_hum_soyabean = 0
	year_sum_precip_soyabean = 0
	year_sum_temp_swheat = 0
	year_sum_hum_swheat = 0
	year_sum_precip_swheat = 0
	year_sum_temp_wwheat = 0
	year_sum_hum_wwheat = 0
	year_sum_precip_wwheat = 0
	optimal_sum_temp_strawberry = optimal_sum_temp_strawberry + year_avg_temp_strawberry
	optimal_sum_hum_strawberry = optimal_sum_hum_strawberry + year_avg_hum_strawberry
	optimal_sum_precip_strawberry = optimal_sum_precip_strawberry + year_avg_precip_strawberry
	optimal_sum_temp_cotton = optimal_sum_temp_cotton + year_avg_temp_cotton
	optimal_sum_hum_cotton = optimal_sum_hum_cotton + year_avg_hum_cotton
	optimal_sum_precip_cotton = optimal_sum_precip_cotton + year_avg_precip_cotton
	optimal_sum_temp_soyabean = optimal_sum_temp_soyabean + year_avg_temp_soyabean
	optimal_sum_hum_soyabean = optimal_sum_hum_soyabean + year_avg_hum_soyabean
	optimal_sum_precip_soyabean = optimal_sum_precip_soyabean + year_avg_precip_soyabean
	optimal_sum_temp_swheat = optimal_sum_temp_swheat + year_avg_temp_swheat
	optimal_sum_hum_swheat = optimal_sum_hum_swheat + year_avg_hum_swheat
	optimal_sum_precip_swheat = optimal_sum_precip_swheat + year_avg_precip_swheat
	optimal_sum_temp_wwheat = optimal_sum_temp_wwheat + year_avg_temp_wwheat
	optimal_sum_hum_wwheat = optimal_sum_hum_wwheat + year_avg_hum_wwheat
	optimal_sum_precip_wwheat = optimal_sum_precip_wwheat + year_avg_precip_wwheat
if optimal_sum_temp_strawberry == 0:
	optimal_avg_temp_strawberry = 0
else:
	optimal_avg_temp_strawberry = optimal_sum_temp_strawberry/1
if optimal_sum_hum_strawberry == 0:
	optimal_avg_hum_strawberry = 0
else:
	optimal_avg_hum_strawberry = optimal_sum_hum_strawberry/1
if optimal_sum_precip_strawberry == 0:
	optimal_avg_precip_strawberry = 0
else:
	optimal_avg_precip_strawberry = optimal_sum_precip_strawberry/1
if optimal_sum_temp_cotton == 0:
	optimal_avg_temp_cotton = 0
else:
	optimal_avg_temp_cotton = optimal_sum_temp_cotton/1
if optimal_sum_hum_cotton == 0:
	optimal_avg_hum_cotton = 0
else:
	optimal_avg_hum_cotton = optimal_sum_hum_cotton/1
if optimal_sum_precip_cotton == 0:
	optimal_avg_precip_cotton = 0
else:
	optimal_avg_precip_cotton = optimal_sum_precip_cotton/1
if optimal_sum_temp_soyabean == 0:
	optimal_avg_temp_soyabean = 0
	optimal_avg_temp_corn = 0
else:
	optimal_avg_temp_soyabean = optimal_sum_temp_soyabean/1
	optimal_avg_temp_corn = optimal_sum_temp_soyabean/1
if optimal_sum_hum_soyabean == 0:
	optimal_avg_hum_soyabean = 0
	optimal_avg_hum_corn = 0
else:
	optimal_avg_hum_soyabean = optimal_sum_hum_soyabean/1
	optimal_avg_hum_corn = optimal_sum_hum_soyabean/1
if optimal_sum_precip_soyabean == 0:
	optimal_avg_precip_soyabean = 0
	optimal_avg_precip_corn = 0
else:
	optimal_avg_precip_soyabean = optimal_sum_precip_soyabean/1
	optimal_avg_precip_corn = optimal_sum_precip_soyabean/1
if optimal_sum_temp_swheat == 0:
	optimal_avg_temp_swheat = 0
else:
	optimal_avg_temp_swheat = optimal_sum_temp_swheat/1
if optimal_sum_hum_swheat == 0:
	optimal_avg_hum_swheat = 0
else:
	optimal_avg_hum_swheat = optimal_sum_hum_swheat/1
if optimal_sum_precip_swheat == 0:
	optimal_avg_precip_swheat = 0
else:
	optimal_avg_precip_swheat = optimal_sum_precip_swheat/1
if optimal_sum_temp_wwheat == 0:
	optimal_avg_temp_wwheat = 0
else:
	optimal_avg_temp_wwheat = optimal_sum_temp_wwheat/1
if optimal_sum_hum_wwheat == 0:
	optimal_avg_hum_wwheat = 0
else:
	optimal_avg_hum_wwheat = optimal_sum_hum_wwheat/1
if optimal_sum_precip_wwheat == 0:
	optimal_avg_precip_wwheat = 0
else:
	optimal_avg_precip_wwheat = optimal_sum_precip_wwheat/1
print "Winter Wheat Average Temperature: %d" % optimal_avg_temp_wwheat
print "Winter Wheat Average Humidity: %d" % optimal_avg_hum_wwheat
print "Winter Wheat Average Precipitation: %f" % optimal_avg_precip_wwheat
print "Spring Wheat Average Temperature: %d" % optimal_avg_temp_swheat
print "Spring Wheat Average Humidity: %d" % optimal_avg_hum_swheat
print "Spring Wheat Average Precipitation: %f" % optimal_avg_precip_swheat
print "Soybean Average Temperature: %d" % optimal_avg_temp_soyabean
print "Soybean Average Humidity: %d" % optimal_avg_hum_soyabean
print "Soybean Average Preciptation: %f" % optimal_avg_precip_soyabean
print "Cotton Average Temperature: %d" % optimal_avg_temp_cotton
print "Cotton Average Humidity: %d" % optimal_avg_hum_cotton
print "Cotton Average Precipitation: %f" % optimal_avg_precip_cotton
print "Corn Average Temperature: %d" % optimal_avg_temp_corn
print "Corn Average Humidity: %d" % optimal_avg_hum_corn
print "Corn Average Precipitation: %f" % optimal_avg_precip_corn
print "Strawberry Average Temperature: %d" % optimal_avg_temp_strawberry
print "strawberry Average Humidity: %d" % optimal_avg_hum_strawberry
print "Strawberry Average Precipitation: %f" % optimal_avg_precip_strawberry
