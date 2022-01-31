import csv
with open('departments.csv', newline='') as csvfile:
 data = csv.DictReader(csvfile)
 print("id Department")
 print("---------------------------------")
 for r in data:
   print(r['department_id']," ",r['department_name'])
