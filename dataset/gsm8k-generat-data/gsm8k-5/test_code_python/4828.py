def solution():
    initial_money = 20  # John had $20
    spent_on_snacks = initial_money * (1/5)  # John spent 1/5 of his money on snacks
    remaining_money = initial_money - spent_on_snacks  # John has this much money remaining after buying snacks
    spent_on_necessities = remaining_money * (3/4)  # John spent 3/4 of his remaining money on necessities

    # Calculate how much money John has left
    money_left = remaining_money - spent_on_necessities
    result = money_left
    return result

print(solution())