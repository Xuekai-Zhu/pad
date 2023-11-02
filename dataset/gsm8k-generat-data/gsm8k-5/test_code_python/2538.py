def solution():
    # Convert total cents (175) to the number of nickels
    total_nickels = 175 // 5

    # Calculate the number of nickels Ray gave to Peter
    nickels_to_peter = 30 // 5

    # Calculate the number of cents Ray gave to Randi
    cents_to_randi = nickels_to_peter * 2 * 5

    # Calculate the number of nickels Ray gave to Randi
    nickels_to_randi = cents_to_randi // 5

    # Calculate the difference in the number of nickels between Randi and Peter
    difference_in_nickels = nickels_to_randi - nickels_to_peter
    result = difference_in_nickels
    return result

print(solution())