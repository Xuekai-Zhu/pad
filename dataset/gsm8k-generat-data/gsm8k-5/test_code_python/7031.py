def solution():
    starting_amount = 600  # Darwin starts with $600
    gas_cost = starting_amount / 3  # Darwin spends 1/3 of his money on gas
    remaining_amount = starting_amount - gas_cost  # Darwin has this much money left
    food_cost = remaining_amount / 4  # Darwin spends 1/4 of what's left on food
    final_amount = remaining_amount - food_cost  # This is the money Darwin has left
    result = final_amount
    return result

print(solution())