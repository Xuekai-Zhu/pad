def solution():
    starting_money = 960  # Derek starts with $960
    textbooks_cost = starting_money / 2  # Derek spends half his money on textbooks
    remaining_money = starting_money - textbooks_cost  # Derek has this much money left after buying textbooks
    school_supplies_cost = remaining_money / 4  # Derek spends a quarter of his remaining money on school supplies
    money_left = remaining_money - school_supplies_cost  # Derek has this much money left after buying school supplies
    result = money_left
    return result

print(solution())