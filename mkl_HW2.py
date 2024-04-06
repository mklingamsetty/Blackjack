from p1_random import P1Random
random = P1Random()

gameCounter = 1
playerHand = 0
dealerHand = 0
playerWins = 0
dealerWins = 0
ties = 0
invalid = 0

print(f"START GAME #{gameCounter}")

while True:
    if(invalid == 0):
        my_number = random.next_int(13) + 1

        if(my_number > 10):
            playerHand += 10
        else:
            playerHand += my_number

        if(my_number == 1):
            print("\nYour card is a ACE!")
        elif((2 <= my_number) and (my_number <= 10)):
            print(f"\nYour card is a {my_number}!")
        elif (my_number == 11):
            print("\nYour card is a JACK!")
        elif (my_number == 12):
            print("\nYour card is a QUEEN!")
        elif (my_number == 13):
            print("\nYour card is a KING!")

        print("Your hand is:", playerHand)

    if ((playerHand >= 21) or (playerHand == 21)):
        gameCounter += 1

        if (playerHand == 21):
            playerWins += 1
            print("\nBLACKJACK! You win!")
            print("")

        elif (playerHand > 21):
            print("\nYou exceeded 21! You lose.\n")
            dealerWins += 1

        playerHand = 0
        dealerHand = 0
        print(f"START GAME #{gameCounter}")

        my_number = random.next_int(13) + 1

        if (my_number > 10):
            playerHand += 10
        else:
            playerHand += my_number

        if (my_number == 1):
            print("\nYour card is a ACE!")
        elif ((2 <= my_number) and (my_number <= 10)):
            print(f"\nYour card is a {my_number}!")
        elif (my_number == 11):
            print("\nYour card is a JACK!")
        elif (my_number == 12):
            print("\nYour card is a QUEEN!")
        elif (my_number == 13):
            print("\nYour card is a KING!")

        print("Your hand is:", playerHand)

    print("\n1. Get another card\n2. Hold hand\n3. Print statistics\n4. Exit")
    user_input = int(input(("\nChoose an option: ")))

    if(user_input == 1):
        invalid = 0
        #print("playerHand inside choice 1:", playerHand)
        continue

    elif(user_input == 2):
        invalid = 0

        dealerHand = random.next_int(11) + 16
        if((dealerHand > 21) or (dealerHand < playerHand)):
            gameCounter += 1
            playerWins += 1
            print("\nDealer's hand:", dealerHand)
            print("Your hand is:", playerHand)
            print("\nYou win!\n")

        elif(dealerHand <= 21 and dealerHand > playerHand):
            dealerWins += 1
            gameCounter += 1
            print("\nDealer's hand:", dealerHand)
            print("Your hand is:", playerHand)
            print("\nDealer wins!\n")

        elif(dealerHand == playerHand):
            ties += 1
            gameCounter += 1
            print("\nDealer's hand:", dealerHand)
            print("Your hand is:", playerHand)
            print("\nIt's a tie! No one wins!\n")

        playerHand = 0
        dealerHand = 0
        print(f"START GAME #{gameCounter}")
        continue


    elif(user_input == 3):
        invalid += 1
        print("\nNumber of Player wins:", playerWins)
        print("Number of Dealer wins:", dealerWins)
        print("Number of tie games:", ties)
        print("Total # of games played is:", gameCounter-1)
        print("Percentage of Player wins:", ((playerWins)/(gameCounter-1))*100, "%")

        continue

    elif(user_input == 4):
        invalid = 0

        break

    else:
        invalid += 1
        print("\nInvalid input!")
        print("Please enter an integer value between 1 and 4.")