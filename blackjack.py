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
loadingValue = -5
card1Control = True
card2Control = True


def clear():
    os.system('cls')


def userAdder(pCount):
    """It adds users to the 'userList' as the person count given."""
    for place in range(0, pCount):
        userList.append({"Name": input("Your Name?\n"),
                        "Value": int(input("Your Total Cash Value?\n")), "Points": 0, "Disq": "none"})
        clear()
    print("Participians\n------------")

    for place in range(1, pCount+1):
        print(userList[place]["Name"], "joined with $",
              userList[place]["Value"])


def bidPicker(pCount):
    """It adds bids to the 'userBidAmount as the bid amount given."""
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
    """It adds random cards to the userRandomCards as the desired amount and computes the points who wins and who loses the game."""
    n = 3
    computer = userList[0]

    # Computers Cards
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

            # Our Random Cards
            userRandomCards.append({"card1": cards[cardRandomerList[random.randint(
                0, 12)]], "card2": cards[cardRandomerList[random.randint(0, 12)]]})
            if pointChecker:
                userList[place]["Points"] += userRandomCards[place]["card1"] + \
                    userRandomCards[place]["card2"]
                pointChecker = False

            point = userList[place]["Points"]

            if userRandomCards[place]["card1"] == 1 and card1Control:
                print(
                    f"Your current point is {point} if you choose 11, your point is going to be {point +10}")
                if input("you have an 'A' in Card 1, do you want 11 or 1?\n") == 11:
                    userRandomCards[place]["card1"] = 11
                    userList[place]["Points"] += 10
                    point = userList[place]["Points"]
                    card1Control = False

            if userRandomCards[place]["card2"] == 1 and card2Control:
                print(
                    f"Your current point is {point} if you choose 11, your point is going to be {point +10}")
                if input("You have an 'A' in Card 2, do you want 11 or 1?\n") == 11:
                    userRandomCards[place]["card2"] = 11
                    userList[place]["Points"] += 10
                    point = userList[place]["Points"]
                    card2Control = False
            print(
                f"{person}, with ${bidAmount} ---> {userRandomCards[place]}\nyour total point is {point}")

            if input("Do you want to get another card?(y or n)\n") == "y":
                userRandomCards[place][f"card{cardCounter}"] = cards[cardRandomerList[random.randint(
                    0, 12)]]
                userList[place]["Points"] += userRandomCards[place][f"card{cardCounter}"]

                currentCard = userRandomCards[place][f"card{cardCounter}"]
                if currentCard == 1:
                    print(
                        f"Your current point is {point} if you choose 11, your point is going to be {point +10}")
                    if input(f"You have an 'A' in Card {cardCounter}, do you want 11 or 1?\n") == 11:
                        userRandomCards[place][f"card{cardCounter}"] = 11
                        userList[place]["Points"] += 10
                        point = userList[place]["Points"]

                cardCounter += 1

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
    time.sleep(4)
    clear()
    winners = 0
    totalBid = 0
    for place in range(1, pCount+1):
        if userList[place]["Disq"] == "prizeWinner":
            winners += 1
            totalBid += userBidAmount[place-1]["bidAmount"]
    if winners == 0:
        bankPoint = userList[0]["Points"]
        print(f"Bank made {bankPoint}, No winners here :/\n")
        givenPrize = 0
    else:
        givenPrize = totalBid / winners
        computer["Value"] -= totalBid
        print("Winners\n-------")
        for place in range(1, pCount+1):
            if userList[place]["Disq"] == "prizeWinner":
                userList[place]["Value"] += givenPrize
                userBidAmount[place-1]["bidAmount"] = 0
                print(userList[place]["Name"],
                      "is winner! Total gain is", givenPrize)


print("Welcome to Blackjack game!")
personCount = int(input("How many players you are?\n"))
userAdder(personCount)
time.sleep(3+personCount*2)
clear()

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


while _:
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

    print("Current Situations")
    for person in range(0, len(userList)):
        name = userList[person]["Name"]
        value = userList[person]["Value"]
        if person == 0:
            print(f"Bank has ${value} in the safe")
        else:
            print(
                f"{name} has left ${value} in total")

    time.sleep(5+personCount*5)
    if session >= 5:
        break
