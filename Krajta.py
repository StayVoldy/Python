
#*** COVID DATABASE STUFF***

f = open("COVID-19.csv", "r")

def daily_max_in_CZ():
    max_daily_in_CR = 0    
    for line in f:
        splitted = line.split(";")
        if splitted[7] == "CZ":
            daily_infected_in_CR = int(splitted[4])
            if daily_infected_in_CR > max_daily_in_CR:
                max_daily_in_CR = daily_infected_in_CR
    print("Max daily infected in CR :", max_daily_in_CR)

def daily_max_in(country):
    max_daily_in_country = 0
    for line in f:
        splitted = line.split(";")
        if splitted[7] == country:
            daily_infected_in_country = int(splitted[4])
            if daily_infected_in_country > max_daily_in_country:
                max_daily_in_country = daily_infected_in_country
                daily_max_date = splitted[0]
    print("Max daily infected in",country,":", max_daily_in_country, "was at:", daily_max_date)

def max_infected_in(date):
    max_in_date = 0
    for line in f:
        splitted = line.split(";")
        if splitted[0] == date:
            infected_in_date = int(splitted[4])
            if infected_in_date > max_in_date:
                max_in_date = infected_in_date
                max_in_date_country = splitted[6]
    print("The worst country in", date, "is", max_in_date_country, "with", max_in_date, "new infected")

#daily_max_in_CZ()
#daily_max_in("SK")
max_infected_in("05.03.2020")    #DD.MM.YYYY