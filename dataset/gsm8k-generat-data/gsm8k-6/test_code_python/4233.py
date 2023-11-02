def solution():
    # Calculate the total amount of potatoes needed in pounds
    total_potatoes = 1.5 * 40

    # Calculate the number of bags of potatoes needed
    num_bags = total_potatoes / 20

    # Calculate the total cost of the potatoes
    total_cost = num_bags * 5
    result = total_cost
    return result

print(solution())