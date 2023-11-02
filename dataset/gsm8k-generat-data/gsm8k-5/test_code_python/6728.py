def solution():
    michael_money = 42  # Michael has $42
    brother_money = 17  # Michael's brother has $17

    # Michael gives away half his money to his brother
    brother_money += michael_money / 2

    # Brother buys $3 worth of candy
    brother_money -= 3

    result = brother_money
    return result

print(solution())