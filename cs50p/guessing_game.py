import random

name = input("what's your name? ").strip().title()
y = random.randint(1, 100)
count = 10
while count > 0:
    x = int(input(f"Hello {name}! 1~100 Your number? "))
    count = count - 1
    print(f"You have {count} chances left")
    if x < y:
        print("too small")
    elif x > y:
        print("too large")
    else:
        print(f"Yes! You used {10 - count} times")
        break
else:
    print(f"Game over! The answer was {y}")