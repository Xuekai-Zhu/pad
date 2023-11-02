def solution():
    
    # Define the weight of the 1959 penny
    1959_weight = 48

    # Calculate the weight of the 2010 penny
    penny_2010_weight = 1959_weight * 0.75

    # Calculate the combined weight of the two pennies
    combined_weight = 1959_weight + penny_2010_weight + 1959_weight

    # Display the combined weight
    result = combined_weight
    return result

print(solution())