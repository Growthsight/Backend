#!/usr/bin/python
import sys
import forecastio
import datetime

api_key = "d0a9649adb009078a10d5fbc96b09409"
day_avg_temp = 0
day_sum_temp = 0
month_avg_temp = 0
month_sum_temp = 0
year_avg_temp = 0
year_sum_temp = 0
optimal_sum_temp = 0
optimal_avg_temp = 0
day_avg_hum = 0
day_sum_hum = 0
month_avg_hum = 0
month_sum_hum = 0
year_avg_hum = 0
year_sum_hum = 0
optimal_sum_hum = 0
optimal_avg_hum = 0
day_avg_precip = 0
day_sum_precip = 0
month_avg_precip = 0
month_sum_precip = 0
year_avg_precip = 0
year_sum_precip = 0
optimal_sum_precip = 0
optimal_avg_precip = 0
temp_error = 0
hum_error = 0
precip_error = 0
for year in range(2000,2016):	
	for month in range(8,9):
		for day in range(1,29):
			current_time = datetime.datetime(year,month,day)
			forecast = forecastio.load_forecast(api_key,sys.argv[1],sys.argv[2],time=current_time)
			byHour = forecast.hourly()
			for j in range(0,24):
				try:
					day_sum_temp = day_sum_temp + byHour.data[j].temperature
				except AttributeError:
					temp_error = temp_error + 1
				try:
					day_sum_hum = day_sum_hum + byHour.data[j].humidity*100
				except AttributeError:
					hum_error = hum_error + 1
				try:
					day_sum_precip = day_sum_precip + byHour.data[j].precipIntensity
				except AttributeError:
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
		year_sum_temp = year_sum_temp + month_avg_temp
		year_sum_hum = year_sum_hum + month_avg_hum
		year_sum_precip = year_sum_precip + month_avg_precip
	if year_sum_temp == 0:
		year_avg_temp = 0
	else:
		year_avg_temp = year_sum_temp/1
	if year_sum_hum == 0:
		year_avg_hum = 0
	else:
		year_avg_hum = year_sum_hum/1
	if year_sum_precip == 0:
		year_avg_precip = 0
	else:
		year_avg_precip = year_sum_precip/1
	year_sum_temp = 0
	year_sum_hum = 0
	year_sum_precip = 0
	optimal_sum_temp = optimal_sum_temp + year_avg_temp
	optimal_sum_hum = optimal_sum_hum + year_avg_hum
	optimal_sum_precip = optimal_sum_precip + year_avg_precip
if optimal_sum_temp == 0:
	optimal_avg_temp = 0
else:
	optimal_avg_temp = optimal_sum_temp/16
if optimal_sum_hum == 0:
	optimal_avg_hum = 0
else:
	optimal_avg_hum = optimal_sum_hum/16
if optimal_sum_precip == 0:
	optimal_avg_precip = 0
else:
	optimal_avg_precip = optimal_sum_precip/16
print optimal_avg_temp
print optimal_avg_hum
print optimal_avg_precip
