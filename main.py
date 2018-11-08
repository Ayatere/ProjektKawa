from tank import Tank
from pump import Pump
from valve import Valve
from stirrer import Stirrer
from heater import Heater
import time

tanks = [Tank(500, False, False, Valve(10, 2)),
         Tank(1000, False, Heater(100), False),
         Tank(1000, Stirrer(10), False, Valve(50, 4)),
         Tank(1000, False, False, False),
         Tank(500, False, False, False)]
pumps = [Pump(30, [1, 2]),
         Pump(20, [3, 2])]
dTime = time.time()

while True:
    try:
        amount = int(input("Write how much coffee do you want(ml)"))
    except ValueError:
        print("Not an number!")
        continue
    else:
        if amount > 1000:
            print("This is too much, choose amount up to 1000ml")
            continue
        break

while True:
    try:
        milk = int(input("Write how much milk in coffee do you want(ml) - can't excede previous number"))
    except ValueError:
        print("Not an number!")
        continue
    else:
        if milk > amount:
            print("This is too much, choose amount up to {}ml".format(amount))
            continue
        break

while True:

    if time.time() - dTime > 0.1:
        dTime = time.time()
        print("working")
    time.sleep(0.01)
