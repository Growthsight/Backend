#!/usr/bin/python
import sys
import forecastio
import datetime

''' KEY FOR THE API TO WORK'''
api_key = "d0a9649adb009078a10d5fbc96b09409"

''' DECLARE VARIABLE WITH INITAIL VALUE TO 0'''
day_avg_temp = 0
day_sum_temp = 0
month_avg_temp = 0
month_sum_temp = 0
year_avg_temp_soyabean = 0
year_avg_temp_swheat = 0
year_avg_temp_wwheat = 0
year_sum_temp_soyabean = 0
year_sum_temp_swheat = 0
year_sum_temp_wwheat = 0
optimal_avg_temp_soyabean = 0
optimal_avg_temp_corn = 0
optimal_avg_temp_swheat = 0
optimal_avg_temp_wwheat = 0
optimal_sum_temp_soyabean = 0
optimal_sum_temp_swheat = 0
optimal_sum_temp_wwheat = 0
day_avg_hum = 0
day_sum_hum = 0
month_avg_hum = 0
month_sum_hum = 0
year_avg_hum_soyabean = 0
year_avg_hum_swheat = 0
year_avg_hum_wwheat = 0
year_sum_hum_soyabean = 0
year_sum_hum_swheat = 0
year_sum_hum_wwheat = 0
optimal_avg_hum_soyabean = 0
optimal_avg_hum_corn = 0
optimal_avg_hum_swheat = 0
optimal_avg_hum_wwheat = 0
optimal_sum_hum_soyabean = 0
optimal_sum_hum_swheat = 0
optimal_sum_hum_wwheat = 0
day_avg_precip = 0
day_sum_precip = 0
month_avg_precip = 0
month_sum_precip = 0
year_avg_precip_soyabean = 0
year_avg_precip_swheat = 0
year_avg_precip_wwheat = 0
year_sum_precip_soyabean = 0
year_sum_precip_swheat = 0
year_sum_precip_wwheat = 0
optimal_avg_precip_soyabean = 0
optimal_avg_precip_corn = 0
optimal_avg_precip_swheat = 0
optimal_avg_precip_wwheat = 0
optimal_sum_precip_soyabean = 0
optimal_sum_precip_swheat = 0
optimal_sum_precip_wwheat = 0

''' VARIABLES TO CALCULATE NUMBER OF DATA POINTS THAT DOES NOT EXIST'''
temp_error = 0
hum_error = 0
precip_error = 0

'''LOOPING THROUGH DIFFERENT YEARS'''
for year in range(2000,2005):	
	'''LOOPING THROUGH DIFFERENT MONTHS'''
	for month in range(4,11):
		'''LOOPING THROUGH DIFFERENT DAYS'''
		for day in range(1,29):
			current_time = datetime.datetime(year,month,day)					#CALCULATE SPECIFIC DAY
			forecast = forecastio.load_forecast(api_key,sys.argv[1],sys.argv[2],time=current_time)	#API CALL FOR SPECIFIC DAY	
			byHour = forecast.hourly()								#HOURLY DATA OBJECT
			'''LOOPING THOUGH DIFFERENT HOURS'''
			for hours in range(0,24):								#24 Hour DATA
				try:
					day_sum_temp = day_sum_temp + byHour.data[hours].temperature
				except AttributeError:							#EXCEPTION HANDLING IF NO DATAPOINT
					temp_error = temp_error + 1
				try:
					day_sum_hum = day_sum_hum + byHour.data[hours].humidity*100
				except AttributeError:							#EXCEPTION HANDLING IF NO DATAPOINT
					hum_error = hum_error + 1
				try:
					day_sum_precip = day_sum_precip + byHour.data[hours].precipIntensity
				except AttributeError:							#EXCEPTION HANDLING IF NO DATAPOINT
					precip_error = precip_error + 1
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
	year_sum_temp_soyabean = 0
	year_sum_hum_soyabean = 0
	year_sum_precip_soyabean = 0
	year_sum_temp_swheat = 0
	year_sum_hum_swheat = 0
	year_sum_precip_swheat = 0
	year_sum_temp_wwheat = 0
	year_sum_hum_wwheat = 0
	year_sum_precip_wwheat = 0
	optimal_sum_temp_soyabean = optimal_sum_temp_soyabean + year_avg_temp_soyabean
	optimal_sum_hum_soyabean = optimal_sum_hum_soyabean + year_avg_hum_soyabean
	optimal_sum_precip_soyabean = optimal_sum_precip_soyabean + year_avg_precip_soyabean
	optimal_sum_temp_swheat = optimal_sum_temp_swheat + year_avg_temp_swheat
	optimal_sum_hum_swheat = optimal_sum_hum_swheat + year_avg_hum_swheat
	optimal_sum_precip_swheat = optimal_sum_precip_swheat + year_avg_precip_swheat
	optimal_sum_temp_wwheat = optimal_sum_temp_wwheat + year_avg_temp_wwheat
	optimal_sum_hum_wwheat = optimal_sum_hum_wwheat + year_avg_hum_wwheat
	optimal_sum_precip_wwheat = optimal_sum_precip_wwheat + year_avg_precip_wwheat
if optimal_sum_temp_soyabean == 0:
	optimal_avg_temp_soyabean = 0
	optimal_avg_temp_corn = 0
else:
	optimal_avg_temp_soyabean = optimal_sum_temp_soyabean/16
	optimal_avg_temp_corn = optimal_sum_temp_soyabean/16
if optimal_sum_hum_soyabean == 0:
	optimal_avg_hum_soyabean = 0
	optimal_avg_hum_corn = 0
else:
	optimal_avg_hum_soyabean = optimal_sum_hum_soyabean/16
	optimal_avg_hum_corn = optimal_sum_hum_soyabean/16
if optimal_sum_precip_soyabean == 0:
	optimal_avg_precip_soyabean = 0
	optimal_avg_precip_corn = 0
else:
	optimal_avg_precip_soyabean = optimal_sum_precip_soyabean/16
	optimal_avg_precip_corn = optimal_sum_precip_soyabean/16
if optimal_sum_temp_swheat == 0:
	optimal_avg_temp_swheat = 0
else:
	optimal_avg_temp_swheat = optimal_sum_temp_swheat/16
if optimal_sum_hum_swheat == 0:
	optimal_avg_hum_swheat = 0
else:
	optimal_avg_hum_swheat = optimal_sum_hum_swheat/16
if optimal_sum_precip_swheat == 0:
	optimal_avg_precip_swheat = 0
else:
	optimal_avg_precip_swheat = optimal_sum_precip_swheat/16
if optimal_sum_temp_wwheat == 0:
	optimal_avg_temp_wwheat = 0
else:
	optimal_avg_temp_wwheat = optimal_sum_temp_wwheat/16
if optimal_sum_hum_wwheat == 0:
	optimal_avg_hum_wwheat = 0
else:
	optimal_avg_hum_wwheat = optimal_sum_hum_wwheat/16
if optimal_sum_precip_wwheat == 0:
	optimal_avg_precip_wwheat = 0
else:
	optimal_avg_precip_wwheat = optimal_sum_precip_wwheat/16
print "winter wheat temp" % optimal_avg_temp_wwheat
print "winter wheat hum" % optimal_avg_hum_wwheat
print "winter wheat precip" % optimal_avg_precip_wwheat
print "spring wheat temp" % optimal_avg_temp_swheat
print "spring wheat hum" % optimal_avg_hum_swheat
print "spring wheat precip" % optimal_avg_precip_swheat
print "soyabean temp" % optimal_avg_temp_soyabean
print "soyabean hum" % optimal_avg_hum_soyabean
print "soyabean precip" % optimal_avg_precip_soyabean
print "corn temp" % optimal_avg_temp_corn
print "corn hum" % optimal_avg_hum_corn
print "corn precip" % optimal_avg_precip_corn
