def solution():
    
    starting_money = 400
    school_supplies = starting_money / 4
    remaining_money = starting_money - school_supplies
    food_cost = remaining_money / 2
    final_amount = remaining_money - food_cost
    result = final_amount
    return result

print(solution())