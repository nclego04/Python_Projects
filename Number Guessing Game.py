import random
num = random.randint(1,100)
print(num)

print("RULES OF THE GAME")
print("Guess the number between 1 to 100. If the guess is close to the number, you will be told that you are warm.")
print("If the guess is not close to the number, you will be told that you are cold.")
print("If the next guess is closer to the number, you will be told that you are warmer. If the next guess is farther")
print("from the number, you will be told that you are colder. You will be told when your guess equals the number.")
print("\n")

guesses = []
guess = int(input("Take a guess: "))

while guess != num:
    
    guesses.append(guess)
    print(guesses)
    
    while guess < 1 or guess > 100:
        print("OUT OF BOUNDS")
        guess = int(input("Take a guess: "))
    
    if (len(guesses) == 1):
        if (abs(num - guess) <= 10):
            print("WARM!")
        else:
            print("COLD!")
            
    else:
        if (abs(num - guess) <= abs(num - guesses[-2])):
            print("WARMER!")
        else:
            print("COLDER!")
    
    guess = int(input("Take a guess: "))


print(f"You've guessed correctly. It took you {len(guesses) + 1} tries.")