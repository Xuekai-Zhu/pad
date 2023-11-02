def solution():
    # Calculate the cost of 2 chairs and subtract it from the total spent to find the cost of the table
    table_cost = 34
    chair_cost = (56 - table_cost) / 2
    result = chair_cost
    return result

print(solution())