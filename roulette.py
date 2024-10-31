# rigged_roulette.py

import random

def spin_roulette_wheel():
    return random.randint(0, 36)

def play_rigged_roulette():
    print("Welcome to the Rigged Roulette!")
    coins = 1000

    while True:
        print(f"You have {coins} coins.")
        bet_type = input("Choose your bet type (Red/Black, Even/Odd, Straight Up): ")
        
        if bet_type not in ["Red", "Black", "Even", "Odd", "Straight Up"]:
            print("Invalid bet type. Please try again.")
            continue
        
        bet = int(input("Enter your bet (0 to quit): "))
        
        if bet == 0:
            break
        elif bet > coins:
            print("Insufficient coins. Please enter a valid bet.")
            continue
        
        result = spin_roulette_wheel()
        print(f"The ball landed on {result}.")
        
        if bet_type == "Red":
            if result in [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]:
                print("You win!")
                coins += bet
            else:
                print("You lose.")
                coins -= bet
        
        elif bet_type == "Black":
            if result in [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]:
                print("You win!")
                coins += bet
            else:
                print("You lose.")
                coins -= bet
        
        elif bet_type == "Even":
            if result != 0 and result % 2 == 0:
                print("You win!")
                coins += bet
            else:
                print("You lose.")
                coins -= bet
        
        elif bet_type == "Odd":
            if result != 0 and result % 2 != 0:
                print("You win!")
                coins += bet
            else:
                print("You lose.")
                coins -= bet
        
        elif bet_type == "Straight Up":
            number = int(input("Enter the number you want to bet on (0-36): "))
            if number == result:
                print("You win!")
                coins += bet * 10
            else:
                print("You lose.")
                coins -= bet
        
        if coins == 0:
            print("You've run out of coins. Game over!")
            break
    
    print(f"You ended the game with {coins} coins.")
    print("Thank you for playing!")
    print("the creator's github is at htpps://github.com/paulbadmanthereal")

if __name__ == "__main__":
    play_rigged_roulette()