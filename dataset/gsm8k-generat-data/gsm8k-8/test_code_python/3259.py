def solution():
    # Initially, Michael has $42
    michael_money = 42

    # Michael gives away half his money, leaving him with half
    michael_money /= 2

    # Michael's brother receives half, so he also has half
    brother_money = michael_money

    # His brother buys $3 worth of candy, leaving him with $35
    brother_money -= 3
    brother_money = 35

    # To find his initial amount, we reverse the steps
    brother_money += 3
    brother_money *= 2
    result = brother_money
    return result

print(solution())