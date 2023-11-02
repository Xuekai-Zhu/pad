def solution():
    starting_money = 48  # Sid takes $48 with him on the shopping trip
    snacks_cost = 8  # He spent $8 on snacks
    remaining_money = starting_money - snacks_cost  # After buying snacks, he has some money left
    remaining_money_half = remaining_money / 2  # He has $4 more than half of his original money left

    # Calculate the money spent on computer accessories
    computer_accessories_cost = starting_money - remaining_money - snacks_cost - remaining_money_half
    result = computer_accessories_cost
    return result

print(solution())