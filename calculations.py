#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime, re

from pprint import pformat

def validate(date, ga):
	
	return date and ga and re.match(r'(\d){4,4}-(\d){2,2}-(\d){2,2}', date) and re.match(r'(\d){1,2}\+\d', ga)

def ga2days(ga):
	(weeks, days) = ga.split('+')
	return int(weeks)*7+int(days)

def days2ga(days):
	return '{}+{}'.format(days // 7, days % 7)

def create_calendar(date, ga):
	days = ga2days(ga)
	date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
	conception = date-datetime.timedelta(days=days)
	
	start = conception-datetime.timedelta(days=conception.weekday())
	
	cal = []
	day = 0

	while day<42*7:
		row = []
		for d in range(0, 7):
			dd = start + datetime.timedelta(days=day)
			datum = '{}. {}. {}'.format(dd.day, dd.month, dd.year)
			gestage = (dd - conception).days
			color = None
			if gestage == 16*7:
				note = 'AMC'
			elif gestage == 24*7: 
				note = 'UPT'
			else:
				note = None	

			if gestage >= 9*7 and gestage<= 14*7-1:
				color='#cfc'

			if gestage >= 15*7 and gestage<= 18*7-1:
				color='#ffc'


			if gestage>=0:
				gestage = days2ga(gestage)
			else:
				gestage = ''
			row.append({'date': datum, 'ga': gestage, 'note': note, 'color': color})
			day += 1
		cal.append(row)

	data = {'date': date, 'conception': conception, 'ga': ga, 'cal': cal}
	return data
