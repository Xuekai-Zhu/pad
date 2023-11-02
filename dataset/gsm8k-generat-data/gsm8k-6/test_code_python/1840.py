def solution():
    # Calculate the number of nickels Ray initially had
    initial_nickels = 95 // 5  # 95 cents divided by 5 cents (value of 1 nickel)

    # Calculate the number of nickels Ray has left after giving 25 cents to Peter
    nickels_left = (95 - 25) // 5  # 70 cents left, divided by 5 cents (value of 1 nickel)

    # Calculate the number of cents Ray gave to Randi
    cents_to_randi = 2 * 25  # twice as many cents as given to Peter

    # Calculate the number of nickels Ray gave to Randi
    nickels_to_randi = cents_to_randi // 5   # divided by 5 cents (value of 1 nickel)

    # Calculate the total number of nickels Ray has left
    total_nickels_left = nickels_left - nickels_to_randi

    result = total_nickels_left
    return result

print(solution())