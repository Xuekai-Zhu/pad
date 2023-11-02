def solution():
    # Calculate the total cost of Mom's shopping
    total_cost = 2*4 + 2 + 6 + 11  # 2 packs of bananas for €4 each, pears for €2, asparagus for €6 and a chicken for €11
    money_left = 55 - total_cost  # calculate the amount of money Mom has left
    result = money_left
    return result

print(solution())