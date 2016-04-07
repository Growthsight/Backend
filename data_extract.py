#!/usr/bin/python
import sys
import forecastio
import datetime

api_key = "d0a9649adb009078a10d5fbc96b09409"
day_avg_temp = 0
day_sum_temp = 0
month_avg_temp = 0
month_sum_temp = 0
optimal_sum_temp = 0
optimal_avg_temp = 0
day_avg_hum = 0
day_sum_hum = 0
month_avg_hum = 0
month_sum_hum = 0
optimal_sum_hum = 0
optimal_avg_hum = 0
day_avg_precip = 0
day_sum_precip = 0
month_avg_precip = 0
month_sum_precip = 0
optimal_sum_precip = 0
optimal_avg_precip = 0
error = 0
if sys.argv[3] == 'winterwheat':
	for month in range(8,11):
		for day in range(1,29):
			current_time = datetime.datetime(2015,month,day)
			forecast = forecastio.load_forecast(api_key,sys.argv[1],sys.argv[2],time=current_time)
			byHour = forecast.hourly()
			for j in range(0,24):
				day_sum_temp = day_sum_temp + byHour.data[j].temperature
				day_sum_hum = day_sum_hum + byHour.data[j].humidity
				try:
					day_sum_precip = day_sum_precip + byHour.data[j].precipIntensity
				except AttributeError:
					error = error + 1
			day_avg_temp = day_sum_temp/24
			day_avg_hum = day_sum_hum/24
			if day_sum_precip == 0:
				day_avg_precip = 0
			else:
				day_avg_precip = day_sum_precip/(24-error)
			day_sum_temp = 0
			day_sum_hum = 0
			day_sum_precip = 0
			error = 0
			month_sum_temp = month_sum_temp + day_avg_temp
			month_sum_hum = month_sum_hum + day_avg_hum
			month_sum_precip = month_sum_precip + day_avg_precip
		month_avg_temp = month_sum_temp/28
		month_avg_hum = month_sum_hum/28
		if month_sum_precip == 0:
			month_avg_precip = 0
		else:
			month_avg_hum = month_sum_precip/28
		month_sum_temp = 0
		month_sum_hum = 0
		month_sum_precip = 0
		optimal_sum_temp = optimal_sum_temp + month_avg_temp
		optimal_sum_hum = optimal_sum_hum + month_avg_hum
		optimal_sum_precip = optimal_sum_precip + month_avg_precip
	optimal_avg_temp = optimal_sum_temp/3
	optimal_avg_hum = optimal_sum_hum/3
	if optimal_sum_precip == 0:
		optimal_avg_precip = 0
	else:
		optimal_avg_precip = optimal_sum_precip/3
print optimal_avg_temp
print optimal_avg_hum*100
print optimal_avg_precip
