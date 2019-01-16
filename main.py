from tank import Tank
from pump import Pump
from valve import Valve
from stirrer import Stirrer
from heater import Heater
import time

tanks = [Tank(500, False, False, Valve(10, 2)),  # coffee
         Tank(1000, False, Heater(300), False),  # water
         Tank(1000, Stirrer(10), False, Valve(50, 4)),  # main tank
         Tank(1000, False, False, False),  # milk
         Tank(500, False, False, False)]  # cup
pumps = [Pump(30, [1, 2]),  # water -> main tank
         Pump(20, [3, 2])]  # milk -> main tank

flag = 0

dTime = time.time()
dTimeWater = time.time()

while True:  # main loop
    if time.time() - dTime > 0.1:  # 10Hz
        if flag == 0:  # Question about amount of coffee
            try:
                amount = int(input("Write how much coffee do you want(ml)"))
            except ValueError:
                print("Not an number!")
                continue
            else:
                if amount > 500:
                    print("This is too much, choose amount up to 500ml")
                else:
                    flag = 1
        if flag == 1:  # Question about amount of milk in coffee
            try:
                milk = int(input("Write how much milk in coffee do you want(ml) - can't excede previous number"))
            except ValueError:
                print("Not an number!")
                continue
            else:
                if milk > amount:
                    print("This is too much, choose amount up to {}ml".format(amount))
                else:
                    flag = 2
        if flag == 2:  # Checking if there is enough milk
            if milk == 0:
                flag = 3
            elif tanks[3].level > (milk + 100):
                flag = 3
            else:
                print("Don't enough milk. Add milk to milk tank.")
                input("You can do that by clicking enter")
                tanks[3].level = tanks[3].capacity
        if flag == 3:  # Checking if there is enough water
            if tanks[1].level > (amount - milk + 100):
                flag = 5
            else:
                print("Not enough water, pouring from valve")
                dTimeWater = time.time()
                flag = 4
        if flag == 4:  # Adding water to water tank
            if time.time() - dTimeWater > 1:
                flag = 3
            elif tanks[1].level + 10 > tanks[1].capacity:
                print("Water tank is full")
                flag = 3
            else:
                tanks[1].level += 10
                print("Pouring water", tanks[1].level)
        if flag == 5:  # Activating heater
            if not tanks[1].heater.activated:
                tanks[1].heater.set_activated(True)
            else:
                print("Heating water", tanks[1].temperature)
                tanks[1].temperature += tanks[1].heater.heatingPower / tanks[1].level
            if tanks[1].temperature > 90:
                tanks[1].heater.set_activated(False)
                flag = 6
        if flag == 6:  # Adding coffee
            if not tanks[0].valve.open:
                tanks[0].valve.set_open(True)
            else:
                print("Adding coffee")
                tanks[0].level -= tanks[1].level / 15
                flag = 7
        if flag == 7:  # Pour water into main tank
            if tanks[2].level < (amount - milk) and not pumps[0].activated:
                print("Start pumping water into main tank")
                pumps[0].set_activated(True)
            else:
                print("Enough water")
                pumps[0].set_activated(False)
                flag = 8
            if pumps[0].activated:
                pumps[0].action(tanks)
        if flag == 8:  # Pour milk into main tank
            if tanks[2].level < amount and not pumps[1].activated:
                print("Start pumping milk into main tank")
                pumps[1].set_activated(True)
            else:
                print("Enough milk")
                pumps[1].set_activated(False)
                flag = 9
            if pumps[1].activated:
                pumps[1].action(tanks)
        if flag == 9:  # Stir coffee
            if not tanks[2].stirrer.activated:
                tanks[2].stirrer.set_activated(True)
            else:
                for x in range(int(100 / tanks[2].stirrer.mixingSpeed)):
                    print("Stirring coffee")
                    time.sleep(0.1)
                print("Coffee is stirred")
                tanks[2].stirrer.set_activated(False)
                flag = 10
        if flag == 10:  # Pouring coffee into cup
            if not tanks[2].valve.open:
                tanks[2].valve.set_open(True)
            else:
                if tanks[2].level > tanks[2].valve.volumePS:
                    tanks[2].level -= tanks[2].valve.volumePS
                    tanks[4].level += tanks[2].valve.volumePS
                    print("Pouring coffee into cup")
                else:
                    tanks[4].level += tanks[2].level
                    tanks[2].level = 0
                    flag = 11
        if flag == 11:  # Coffee is done
            input("Coffee is done, you can take it by clicking enter")
            tanks[4].level = 0
            flag = 0
        dTime = time.time()
    time.sleep(0.01)
