def solution():
    starting_money = 42
    given_away_money = starting_money / 2
    candy_cost = 3
    remaining_money_after_candy = 35

    # Calculate how much money Michael had left after giving away half to his brother
    michael_remaining_money = starting_money - given_away_money

    # Calculate how much money his brother had before buying candy
    brother_starting_money = michael_remaining_money + remaining_money_after_candy + candy_cost

    result = brother_starting_money
    return result

print(solution())