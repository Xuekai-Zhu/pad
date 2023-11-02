def solution():
    """Macey saves to buy herself a shirt that costs $3. She was able to save $1.50 already. How many weeks does she need to save for the remaining amount if she saves $0.50 per week?"""
    # Define the cost of the shirt and the amount Macey has already saved
    shirt_cost = 3
    saved_amount = 1.5

    # Calculate the remaining amount Macey needs to save
    remaining_amount = shirt_cost - saved_amount

    # Calculate the number of weeks needed to save the remaining amount
    weeks_needed = remaining_amount / 0.5

    # Round up the number of weeks to a whole number
    weeks_needed = math.ceil(weeks_needed)

    result = weeks_needed
    return result

print(solution())