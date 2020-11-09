import random
#* Simple RNG

print("         _____                   _                     _   _                    _                   _____                                 _               ")
print("        | ___ \                 | |                   | \ | |                  | |                 |  __ \                               | |              ")
print("        | |_/ / __ _  _ __    __| |  ___   _ __ ___   |  \| | _   _  _ __ ___  | |__    ___  _ __  | |  \/  ___  _ __    ___  _ __  __ _ | |_  ___   _ __ ")
print("        |    / / _` || '_ \  / _` | / _ \ | '_ ` _ \  | . ` || | | || '_ ` _ \ | '_ \  / _ \| '__| | | __  / _ \| '_ \  / _ \| '__|/ _` || __|/ _ \ | '__|")
print("        | |\ \| (_| || | | || (_| || (_) || | | | | | | |\  || |_| || | | | | || |_) ||  __/| |    | |_\ \|  __/| | | ||  __/| |  | (_| || |_| (_) || |   ")
print("        \_| \_|\__,_||_| |_| \__,_| \___/ |_| |_| |_| \_| \_/ \__,_||_| |_| |_||_.__/  \___||_|     \____/ \___||_| |_| \___||_|   \__,_| \__|\___/ |_|   ")
                                                                                                                                                        
print("\n              Welcome to my RNG")   

minimum = int(input("\n             Please type minimal number: "))
maximum = int(input("\n             Please type maximal number: "))

random_number = random.randint(minimum, maximum)

print("\n \n             Your awesome random number is:", random_number)