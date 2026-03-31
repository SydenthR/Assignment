# Name: Alex Russell
# File Name: loops.py
# Description: This program completes multiple exercises involving conditionals
# and loops, including guessing games and list iteration.


# 4.1
print("---- 4.1 ----")
secret = 7
guess = 5

if guess < secret:
    print("too low")
elif guess > secret:
    print("too high")
else:
    print("just right")
# 4.2
print("\n---- 4.2 ----")
small = True
green = True

if small and green:
    print("pea")
elif small and not green:
    print("cherry")
elif not small and green:
    print("watermelon")
else:
    print("pumpkin")
# 6.1
print("\n---- 6.1 ----")
for num in [3, 2, 1, 0]:
    print(num)
# 6.2
print("\n---- 6.2 ----")
guess_me = 7
number = 1

while True:
    if number < guess_me:
        print("too low")
    elif number == guess_me:
        print("found it!")
        break
    else:
        print("oops")
        break

    number += 1
# 6.3
print("\n---- 6.3 ----")
guess_me = 5

for number in range(10):
    if number < guess_me:
        print("too low")
    elif number == guess_me:
        print("found it!")
        break
    else:
        print("oops")
        break