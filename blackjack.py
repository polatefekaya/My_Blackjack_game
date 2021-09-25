import time
import random
import os


cards = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
         "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}
cardRandomerList = ["A", "2", "3", "4", "5",
                    "6", "7", "8", "9", "10", "J", "Q", "K"]
userList = [{"Name": "Bank", "Value": 0, "Points": 0}]
userBidAmount = []
userRandomCards = []

session = 0
game = True
loadingValue = -5
wGivenPrize = 0


def clear():
    os.system('cls')


def userAdder(pCount):
    for place in range(0, pCount):
        userList.append({"Name": input("Your Name?\n"),
                        "Value": int(input("Your Total Cash Value?\n")), "Points": 0, "Disq": "none"})
        clear()
    print("Participians\n------------")

    for place in range(1, pCount+1):
        print(userList[place]["Name"], "joined with $",
              userList[place]["Value"])


def bidPicker(pCount):
    for place in range(1, pCount+1):
        person = userList[place]["Name"]
        while _:
            bidAmount = int(
                input(f"Hello {person}, what is your bid amount?\n"))
            if bidAmount > userList[place]["Value"]:
                print("Your Bid Amount cannot be higher than total cash amount!")
            else:
                break
        userBidAmount.append(
            {"bidAmount": bidAmount})
        userList[place]["Value"] -= bidAmount
        clear()
    for place in range(0, pCount):
        print(userList[place+1]["Name"], "puts $",
              userBidAmount[place]["bidAmount"], "in this round")
    time.sleep(personCount*2+2)
    clear()


def randomCards(pCount):
    n = 3
    computer = userList[0]

    # Bilgisayarın kartları
    userRandomCards.append({"card1": cards[cardRandomerList[random.randint(
        0, 12)]], "card2": cards[cardRandomerList[random.randint(0, 12)]]})
    userList[0]["Points"] += userRandomCards[0]["card1"] + \
        userRandomCards[0]["card2"]

    while computer["Points"] >= 11:
        userRandomCards[0][f"card{n}"] = cards[cardRandomerList[random.randint(
            0, 12)]]
        computer["Points"] += userRandomCards[0][f"card{n}"]

        if computer["Points"] > 21:
            computer["Points"] -= userRandomCards[0][f"card{n}"]
            break
        n+1
    cCard = userRandomCards[0]["card1"]
    print(f"Computer's cards are {cCard} and ...")
    for place in range(1, pCount+1):
        cardCounter = 3
        pointChecker = True
        computer["Value"] += userBidAmount[place-1]["bidAmount"]
        while _:

            person = userList[place]["Name"]
            bidAmount = userBidAmount[place-1]["bidAmount"]

            # Bizim rastgele kartlarımız
            userRandomCards.append({"card1": cards[cardRandomerList[random.randint(
                0, 12)]], "card2": cards[cardRandomerList[random.randint(0, 12)]]})
            if pointChecker:
                userList[place]["Points"] += userRandomCards[place]["card1"] + \
                    userRandomCards[place]["card2"]
                pointChecker = False
            point = userList[place]["Points"]
            print(
                f"{person}, with ${bidAmount} ---> {userRandomCards[place]}\nyour total point is {point}")

            if input("Do you want to get another card?(y or n)\n") == "y":
                userRandomCards[place][f"card{cardCounter}"] = cards[cardRandomerList[random.randint(
                    0, 12)]]
                userList[place]["Points"] += userRandomCards[place][f"card{cardCounter}"]
                cardCounter += 1
                # print(point)
                # print(userList[place]["Points"])

                if userList[place]["Points"] > 21:
                    print("You disqualified")
                    userList[place]["Disq"] = "Disqualified"

                    bidAmount = 0
                    break

                if cardCounter == 5 and userList[place]["Points"] <= 21:
                    userList[place]["Disq"] = "prizeWinner"

            else:
                if userList[place]["Points"] > computer["Points"] and userList[place]["Points"] <= 21:
                    userList[place]["Disq"] = "prizeWinner"
                else:
                    userList[place]["Disq"] = "Disqualified"
                break

    winners = 0
    for place in range(1, pCount+1):
        if userList[place]["Disq"] == "prizeWinner":
            winners += 1
    if winners == 0:
        print("No winners here :/")
        givenPrize = 0
    else:
        givenPrize = computer["Value"] / winners
        wGivenPrize = givenPrize
        computer["Value"] = 0
    print("Winners\n-------")
    for place in range(1, pCount+1):
        if userList[place]["Disq"] == "prizeWinner":
            userList[place]["Value"] += givenPrize
            userBidAmount[place-1]["bidAmount"] = 0
            print(userList[place]["Name"],
                  "is winner! Total gain is", userList[place]["Value"])


print("Welcome to Blackjack game!")
personCount = int(input("How many players you are?\n"))
userAdder(personCount)
time.sleep(3+personCount*2)
clear()

# son ve önceki total cash sistemöi düzgün çalışmıyor
# Loading part of the game
for _ in range(0, 20):
    loadingValue += random.randint(5, 20)
    if loadingValue >= 100:
        print("Loading %100")
    else:
        print(f"Loading %{loadingValue}")
    if loadingValue >= 100:
        break
    time.sleep(random.uniform(0.05, 1))
    clear()


while game:
    clear()
    session += 1
    print(f"Game Session{session} is Starting")
    time.sleep(2)
    clear()
    if session > 1:
        for place in range(0, personCount+1):
            userList[place]["Points"] = 0
            userList[place]["Disq"] = "none"

        userRandomCards.clear()
        userBidAmount.clear()

    bidPicker(personCount)
    randomCards(personCount)

    # görsel iyileştirmeler yapacağım.
    print("Current Situations")
    for person in range(0, len(userList)):
        name = userList[person]["Name"]
        value = userList[person]["Value"]
        if person == 0:
            print(f"Bank has ${value} in the safe")
        else:
            print(
                f"{name} has left ${value} in total, previous total cash is ${value - wGivenPrize}")

    time.sleep(4+personCount*4)
    if session >= 5:
        break

# keskin hediyelik
