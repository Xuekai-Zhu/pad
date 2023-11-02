def solution():
    num_chairs = 3

    table_cost = 50

    plates_cost = 2 * 20

    total_paid = 130

    change = 4

    # Calculate the total cost of all items except chairs
    total_without_chairs = table_cost + plates_cost

    # Calculate the cost of each chair
    cost_per_chair = (total_paid - change - total_without_chairs) / num_chairs

    result = cost_per_chair
    return result

print(solution())