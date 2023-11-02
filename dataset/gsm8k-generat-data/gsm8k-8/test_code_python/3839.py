def solution():
    # Define the number of nickels Quentavious has
    num_nickels = 5

    # Calculate the total number of gum pieces he can get
    total_gum = num_nickels * 2

    # Calculate the number of nickels he has left after taking 2
    num_nickels_left = num_nickels - 2

    # Calculate the total number of gum pieces he actually got
    actual_gum = num_nickels_left * 2

    result = actual_gum
    return result

print(solution())