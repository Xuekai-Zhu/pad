def solution():
    # Calculate the total cost of the table and plates
    table_cost = 50
    plates_cost = 20 * 2
    total_cost = table_cost + plates_cost

    # Calculate the remaining amount after paying for the table and plates
    remaining_amount = 130 - total_cost - 4

    # Calculate the cost of each chair
    chair_cost = remaining_amount / 3

    result = chair_cost
    return result

print(solution())