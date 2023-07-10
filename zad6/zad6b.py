import csv

def read(file):
 with open(file, 'r', newline='') as filecsv:
  reader = csv.reader(filecsv)
  data = []
  for row in reader:
   data.append(row)
 return data

def print_data(data):
 for row in data:
  print("------")
  print("ID: ", row[0])
  print("Name: ", row[1])
  print("Surname: ", row[2])
  print("City: ", row[3])

def add(data):
 if len(data) == 0:
  id = 1
 else:
  id = int(data[-1][0])+1
 name = input("Name: ")
 surname = input("Surname: ")
 city = input("City: ")
 data.append([id, name, surname, city])
 return data

def save(data):
 with open('file.csv', 'w', newline='') as filecsv:
  writer = csv.writer(filecsv)
  writer.writerows(data)
 exit()

def delete(data):
 id_del = input("Which record you want to delete? Enter id.")
 status = False
 for i in range(0, len(data)):
  if data[i][0] == id_del:
   data.pop(i)
   status = True
 if status == True:
  print("Successful removal")
 else:
  print("There is no such record with id = ", id_del)
 return data

def help():
 print("\nWhat do you want to do? Choose action: \n")
 print("[1] PRINT data \n")
 print("[2] ADD record \n")
 print("[3] DELETE record \n")
 print("[4] SAVE & EXIT \n")
 print("[5] HELP \n")

data = read("file.csv")
print_data(data)
help()

while True:
 num_action = int(input("Which action you want? Enter the number.."))
 if num_action == 1:
  print_data(data)
 elif num_action == 2:
  data = add(data)
 elif num_action == 3:
  data = delete(data)
 elif num_action == 4:
  save(data)
 elif num_action == 5:
  help()
 else:
  print("There is no such action")


