#!/usr/bin/python
import sys
import forecastio
import datetime
import locale
import json
''' KEY FOR THE API TO WORK'''
api_key = "c6a99c6932310919951887873b154cbb"
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
''' DECLARE VARIABLE WITH INITAIL VALUE TO 0'''
arrayofcrops = []
loc_temp = [0,0,0,0,0,0]
loc_precip = [0,0,0,0,0,0]
loc_hum = [0,0,0,0,0,0]
score = [0,0,0,0,0,0]
weighted_ideal = [0,0,0,0,0,0]
weighted_location = [0,0,0,0,0,0]
per_change = [0,0,0,0,0,0]
temp_weights = [0.2,0.2,0.2,0.5,0.3,0.5]
humidity_weights = [0.3,0.3,0.3,0.2,0.5,0.3]
precip_weights = [0.5,0.5,0.5,0.3,0.2,0.2]
arrayofcrops.append({"Crop_Name":"Winter Wheat", "GrowthSight_Score":"0", "Ideal_Humidity": "75", "Ideal_Precipitation": "0.1", "Ideal_Temperature":"46", "Location_Humidity":"70%", "Location_Precipitation":"15", "Location_Temperature":"60", "Planting_Season":"August September October" })
arrayofcrops.append({"Crop_Name":"Spring Wheat", "GrowthSight_Score":"0", "Ideal_Humidity": "75", "Ideal_Precipitation": "0.2", "Ideal_Temperature":"65", "Location_Humidity":"70", "Location_Precipitation":"15", "Location_Temperature":"60", "Planting_Season":"April May"})
arrayofcrops.append({"Crop_Name":"Soybean", "GrowthSight_Score":"0", "Ideal_Humidity": "75", "Ideal_Precipitation": "0.1", "Ideal_Temperature":"69", "Location_Humidity":"70", "Location_Precipitation":"15", "Location_Temperature":"60", "Planting_Season":"April May June"})
arrayofcrops.append({"Crop_Name":"Cotton", "GrowthSight_Score":"0", "Ideal_Humidity": "20", "Ideal_Precipitation": "0.12", "Ideal_Temperature":"84", "Location_Humidity":"70", "Location_Precipitation":"15", "Location_Temperature":"60", "Planting_Season":"March April May June"})
arrayofcrops.append({"Crop_Name":"Corn", "GrowthSight_Score":"0", "Ideal_Humidity": "70", "Ideal_Precipitation": "0.21", "Ideal_Temperature":"66", "Location_Humidity":"70", "Location_Precipitation":"15", "Location_Temperature":"60", "Planting_Season":"April May June"})
arrayofcrops.append({"Crop_Name":"Strawberry", "GrowthSight_Score":"0", "Ideal_Humidity": "80", "Ideal_Precipitation": "0.12", "Ideal_Temperature":"69", "Location_Humidity":"70", "Location_Precipitation":"15", "Location_Temperature":"60", "Planting_Season":"January February March April May"})
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
state = sys.argv[3]
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
	loc_temp[5] = 0
else:
	loc_temp[5] = optimal_sum_temp_strawberry/1
if optimal_sum_hum_strawberry == 0:
	loc_hum[5] = 0
else:
	loc_hum[5] = optimal_sum_hum_strawberry/1
if optimal_sum_precip_strawberry == 0:
	loc_precip[5] = 0
else:
	loc_precip[5] = optimal_sum_precip_strawberry/1
if optimal_sum_temp_cotton == 0:
	loc_temp[3] = 0
else:
	loc_temp[3] = optimal_sum_temp_cotton/1
if optimal_sum_hum_cotton == 0:
	loc_hum[3] = 0
else:
	loc_hum[3] = optimal_sum_hum_cotton/1
if optimal_sum_precip_cotton == 0:
	loc_precip[3] = 0
else:
	loc_precip[3] = optimal_sum_precip_cotton/1
if optimal_sum_temp_soyabean == 0:
	loc_temp[2]= 0
	loc_temp[4] = 0
else:
	loc_temp[2] = optimal_sum_temp_soyabean/1
	loc_temp[4] = optimal_sum_temp_soyabean/1
if optimal_sum_hum_soyabean == 0:
	loc_hum[2] = 0
	loc_hum[4] = 0
else:
	loc_hum[2] = optimal_sum_hum_soyabean/1
	loc_hum[4] = optimal_sum_hum_soyabean/1
if optimal_sum_precip_soyabean == 0:
	loc_precip[2] = 0
	loc_precip[4] = 0
else:
	loc_precip[2] = optimal_sum_precip_soyabean/1
	loc_precip[4] = optimal_sum_precip_soyabean/1
if optimal_sum_temp_swheat == 0:
	loc_temp[1] = 0
else:
	loc_temp[1] = optimal_sum_temp_swheat/1
if optimal_sum_hum_swheat == 0:
	loc_hum[1] = 0
else:
	loc_hum[1] = optimal_sum_hum_swheat/1
if optimal_sum_precip_swheat == 0:
	loc_precip[1] = 0
else:
	loc_precip[1] = optimal_sum_precip_swheat/1
if optimal_sum_temp_wwheat == 0:
	loc_temp[0] = 0
else:
	loc_temp[0] = optimal_sum_temp_wwheat/1
if optimal_sum_hum_wwheat == 0:
	loc_hum[0] = 0
else:
	loc_hum[0] = optimal_sum_hum_wwheat/1
if optimal_sum_precip_wwheat == 0:
	loc_precip[0] = 0
else:
	loc_precip[0] = optimal_sum_precip_wwheat/1

for i in range(0,6):
	arrayofcrops[i]["Location_Temperature"] = loc_temp[i]
	arrayofcrops[i]["Location_Humidity"] = loc_hum[i]
	arrayofcrops[i]["Location_Precipitation"] = loc_precip[i]
for i in range(0,6):
	weighted_ideal[i] = locale.atof(arrayofcrops[i].get("Ideal_Temperature"))*temp_weights[i] + locale.atof(arrayofcrops[i].get("Ideal_Humidity"))*humidity_weights[i] + locale.atof(arrayofcrops[i].get("Ideal_Precipitation"))*precip_weights[i] 
	weighted_location[i] = loc_temp[i]*temp_weights[i] + loc_hum[i]*humidity_weights[i] + loc_precip[i]*precip_weights[i] 

for i in range(0,6):
	per_change[i] = abs(weighted_ideal[i] - weighted_location[i])/weighted_ideal[i]
	if (per_change[i] >0 and per_change[i] <=5):
		score[i] = 10
	elif (per_change[i] >5 and per_change[i] <=10):
		score[i] = 8
	elif (per_change[i] >10 and per_change[i] <=15):
		score[i] = 6
	elif (per_change[i] >15 and per_change[i] <=20):
		score[i] = 4
	elif (per_change[i] >20 and per_change[i] <=25):
		score[i] = 2
	else:
		score[i] = 0
			
for i in range(0,6):
	arrayofcrops[i]["GrowthSight_Score"] = score[i]

final_jason = []
final_jason.append({"state": sys.argv[3],"location_lat": sys.argv[1],"location_long": sys.argv[2],"report": arrayofcrops})
x = json.dumps(final_jason)
print x
