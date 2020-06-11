#!/usr/bin/env python3

import sys
for line in sys.stdin:
	line=line.strip()
	if("Employee ID" in line):
		continue
	line=line.split("\t")
	
	Employee_Id="-1"
	Name="-1"
	Salary="-1"
	Country="-1"
	Passcode=False
	
	if len(line)==4:
		Employee_Id=line[0]
		
		Salary=line[1]
		
		Country=line[2]
		Passcode=line[3]
	else:
		Employee_Id=line[0]
		Name=line[1]
	
	print(Employee_Id,"\t",Salary,"\t",Country,"\t",Passcode,"\t",Name)
