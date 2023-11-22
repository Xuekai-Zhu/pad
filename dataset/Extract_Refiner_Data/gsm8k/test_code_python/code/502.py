def solution():
    
    # Define the number of legs per dog and the cost per pair of snowshoes
    legs_per_dog = 4
    cost_per_pair = 12.00

    # Calculate the total number of legs
    total_legs = 6 * legs_per_dog

    # Calculate the total number of pairs of snowshoes needed
    total_pairs = total_legs / 4

    # Calculate the total cost of the snowshoes
    total_cost = total_pairs * cost_per_pair

    # return the result
    result = total_cost
    return result

print(solution())