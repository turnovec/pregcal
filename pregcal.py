#!/usr/bin/env python 
# -*- coding: utf-8 -*-

from calculations import create_calendar, validate

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def info():
	if request.method == 'POST':

		date = request.form.get('date', None)
		ga = request.form.get('ga', None)
		if validate(date, ga):
			return render_template('cal.html', data = create_calendar(date, ga))		
	
	return render_template('index.html')

if __name__ == '__main__':
	app.run()

