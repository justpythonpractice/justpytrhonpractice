import sys
salary = float(input('Input hourly wage >>'))
hours = 8*5*4
salary_calc = salary * hours
print("your monthly salary of %s hourly wage will be %s, and yearly it will be %s" % (salary, salary_calc, (salary_calc*12)))