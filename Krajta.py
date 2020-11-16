
#*** COVID DATABASE STUFF***

f = open("COVID-19.csv", "r")

def max_in_cz_in_one_day():
    max_daily_in_cz = 0    
    for line in f:
        splitted = line.split(";")
        if splitted[7] == "CZ":
            daily_infected = int(splitted[4])
            if daily_infected >> max_daily_in_cz:
                max_daily_in_cz = daily_infected
    print("Max daily infected:", max_daily_in_cz)

max_in_cz_in_one_day()