def solution():
    
    # Define the amount raised by each person
    keegan_amount = 83
    tasha_amount =91

    # Calculate the total amount raised by both people
    total_amount = keegan_amount + tasha_amount

    # Calculate the amount still needed to reach the goal
    remaining_amount = 200 - total_amount

    # Display the remaining amount needed
    result = remaining_amount
    return result

print(solution())