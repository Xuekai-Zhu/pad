def solution():
    # Convert 175 cents to number of nickels
    num_nickels = 175 // 5

    # Calculate the number of nickels Ray gave to Peter
    nickels_to_peter = 30 // 5

    # Calculate the number of cents Ray gave to Randi
    cents_to_randi = 2 * (30 - nickels_to_peter*5)

    # Calculate the number of nickels Ray gave to Randi
    nickels_to_randi = cents_to_randi // 5

    # Calculate the difference in number of nickels between Randi and Peter
    diff_nickels = nickels_to_randi - nickels_to_peter

    result = diff_nickels
    return result

print(solution())