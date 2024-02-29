checked_out=["Andrea", "Manuel", "Khalid"]
temp_list=[]

with open("guests.txt", "rt") as guests:
    for g in guests:
        temp_list.append(g.strip())

with open("guests.txt", 'w') as guests:
    for name in temp_list:
        if name not in checked_out:
            guests.write(name + "\n")

guests.close()

with open("guests.txt") as guests:
    for line in guests:
        print(line)