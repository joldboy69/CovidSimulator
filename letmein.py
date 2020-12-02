import random
import time

curTime = 0
infected = 2
dead = 0
recovered = 0


while True:
    if infected >= 40000000:
        print("Final Results: ")
        print("Time: " + str(curTime) + " months")
        print("Dead: " + str(dead))
        print("Infected: " + str(infected))
        print("Recovered: " + str(round(recovered)))
        break
    time.sleep(1)
    curTime += 1
    infected += infected * random.randint(1,3)
    chanceOfDie = random.randint(0,2)
    if chanceOfDie == 0 or chanceOfDie ==2:
        pass
    elif chanceOfDie == 1:
        dead += round(infected*0.1)
        recovered += round(infected * 0.9)
    print("Time: " + str(curTime) + " months")
    print("Dead: " + str(dead))
    print("Infected: " + str(infected))
    print("Recovered: " + str(round(recovered)))



