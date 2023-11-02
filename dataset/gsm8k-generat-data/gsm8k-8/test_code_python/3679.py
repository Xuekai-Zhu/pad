def solution():
    # Define the cost of the shirt and the amount Macey has already saved
    shirt_cost = 3
    saved_amount = 1.5

    # Calculate the remaining amount needed to buy the shirt
    remaining_amount = shirt_cost - saved_amount

    # Calculate the number of weeks Macey needs to save for the remaining amount
    weeks_needed = remaining_amount / 0.5
    result = weeks_needed
    return result

print(solution())