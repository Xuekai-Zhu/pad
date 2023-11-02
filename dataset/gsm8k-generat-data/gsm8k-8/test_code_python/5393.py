def solution():
    # Calculate the cost of the kitchen module and two bathroom modules
    kitchen_cost = 20000
    bathroom_cost = 2 * 12000

    # Calculate the area of the remaining modules
    remaining_area = 2000 - 400 - 300

    # Calculate the cost of the remaining modules
    remaining_cost = remaining_area * 100

    # Calculate the total cost
    total_cost = kitchen_cost + bathroom_cost + remaining_cost
    result = total_cost
    return result

print(solution())