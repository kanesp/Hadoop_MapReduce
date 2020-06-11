#!/usr/bin/env python3

import sys
join1_dict={}
join2_dict={}
for line in sys.stdin:
	line=line.strip()
	
	Employee_ID,Salary,Country,Passcode,Name=line.split('\t',4)
	if "False" in Passcode:
		join1_dict[Employee_ID]=[Name]
	else:
		join2_dict[Employee_ID]=[Salary,Country,Passcode]


for Employee_ID in join2_dict.keys():
	Salary=join2_dict[Employee_ID][0]
	Country=join2_dict[Employee_ID][1]
	Passcode=join2_dict[Employee_ID][2]
	Name=join1_dict[Employee_ID][0]
	
	print(Employee_ID,"\t",Name,"\t",Salary,"\t",Country,"\t",Passcode)
	
	
