def solution():
    
    # Define the total amount of coal ordered in kilos
    total_coal = 850

    # Calculate the total number of bags of coal
    total_bags = total_coal / 50

    # Calculate the total cost of the order
    total_cost = total_bags * 18

    # return the result
    result = total_cost
    return result

print(solution())