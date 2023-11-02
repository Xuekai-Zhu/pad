def solution():
    initial_money = 20  # John had $20
    spent_on_snacks = (1/5) * initial_money  # John spent 1/5 of his money on snacks
    remaining_money = initial_money - spent_on_snacks  # John's remaining money after buying snacks
    spent_on_necessities = (3/4) * remaining_money  # John spent 3/4 of the remaining money on necessities
    left_money = remaining_money - spent_on_necessities  # John's left over money after buying necessities
    result = left_money
    return result

print(solution())