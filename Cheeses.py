# 7.4 - 7.6 List Manipulation
things = ["mozzarella", "cinderella", "salmonella"]

things[1] = things[1].capitalize()
print("After capitalizing person:", things)

things[0] = things[0].upper()
print("After making cheese uppercase:", things)

# 9.1 Function returning a list
def good():
    return ['Harry', 'Ron', 'Hermione']


print("\nGood list:", good())

# 9.2 Generator for odd numbers
def get_odds():
    for num in range(10):
        if num % 2 != 0:
            yield num


# Find and print the 3rd odd number
count = 0
for number in get_odds():
    count += 1
    if count == 3:
        print("Third odd number:", number)
        break