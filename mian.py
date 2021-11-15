import requests, random, string, gratient
from os import system
gen = 0
working = 0
nun = 0

system("cls && title Cvip Minecraft Name Gen && mode con:cols=54 lines=30")

lingth = int(input("How Long Do You Want The Name: "))
system("cls")
while True:
    name = ('').join(random.choice(string.ascii_letters + string.digits)for k in range(lingth))
    api = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{name}")

    if api.status_code == 200:
        gen += 1
        nun += 1
        system("title All: "+str(gen)+" Working: "+str(working)+" Not Working: "+str(nun))
        print(gratient.red(f"{name} Was Taken"))
    else:
        gen += 1
        working += 1
        system("title All: "+str(gen)+" Working: "+str(working)+" Not Working: "+str(nun))
        print(gratient.green(f"{name} Not Taken"))
        with open("names.txt", "a") as f:
            f.write(f"{name}\n")
            f.close
