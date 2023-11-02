def solution():
    num_chocolate = 10  # 10 kids want chocolate doughnuts
    num_glazed = 15  # 15 kids want glazed doughnuts
    cost_chocolate = 2  # Chocolate doughnuts cost $2 each
    cost_glazed = 1  # Glazed doughnuts cost $1 each

    # Calculate the total cost for chocolate doughnuts
    total_chocolate_cost = num_chocolate * cost_chocolate

    # Calculate the total cost for glazed doughnuts
    total_glazed_cost = num_glazed * cost_glazed

    # Calculate the overall total cost
    total_cost = total_chocolate_cost + total_glazed_cost
    result = total_cost
    return result

print(solution())