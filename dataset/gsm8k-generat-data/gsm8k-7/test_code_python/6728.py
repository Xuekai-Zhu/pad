def solution():
    michael_money = 42
    brother_money = 17

    # Michael gives away half of his money to his brother
    michael_money = michael_money / 2
    brother_money = brother_money + michael_money

    # Brother buys $3 worth of candy
    brother_money = brother_money - 3

    result = brother_money
    return result

print(solution())