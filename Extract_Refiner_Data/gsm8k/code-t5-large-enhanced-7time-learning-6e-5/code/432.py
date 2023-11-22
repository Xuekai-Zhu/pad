def solution():
    
    # Define the weight of the cake in ounces
    cake_weight = 20

    # Calculate the total weight of the cake
    total_weight = cake_weight / 8

    # Calculate the weight of the remaining cake
    remaining_weight = total_weight - (2 * 8)

    # Display the weight of the remaining cake
    result = remaining_weight
    return result

print(solution())