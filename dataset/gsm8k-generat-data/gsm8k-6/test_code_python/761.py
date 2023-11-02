def solution():
    # Calculate the total cost of Joan's purchases
    total_cost = (2*5) + 20 + 10 + 10  # cost of hummus, chicken, bacon, and vegetables
    # Calculate the amount of money Joan has left
    remaining_money = 60 - total_cost
    # Calculate the number of apples Joan can purchase with her remaining money
    num_apples = remaining_money // 2
    result = num_apples
    return result

print(solution())