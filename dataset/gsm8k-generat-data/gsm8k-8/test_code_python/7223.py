def solution():
    # Define the amount and cost of meat
    meat_amount = 2
    meat_cost = 82

    # Calculate the total cost of meat
    total_cost = meat_amount * meat_cost

    # Calculate the remaining money after buying the meat
    remaining_money = 180 - total_cost
    result = remaining_money
    return result

print(solution())