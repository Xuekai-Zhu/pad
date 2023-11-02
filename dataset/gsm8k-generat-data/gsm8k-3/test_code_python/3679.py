def solution():
    """Macey saves to buy herself a shirt that costs $3. She was able to save $1.50 already. How many weeks does she need to save for the remaining amount if she saves $0.50 per week?"""
    # Define the total cost of the shirt
    total_cost = 3

    # Define the amount already saved
    amount_saved = 1.5

    # Define the amount saved per week
    saved_per_week = 0.5

    # Calculate the remaining amount to be saved
    remaining_amount = total_cost - amount_saved

    # Calculate the number of weeks needed to save the remaining amount
    weeks_needed = remaining_amount / saved_per_week

    # Round up to the nearest week
    weeks_needed = math.ceil(weeks_needed)

    # Display the number of weeks needed
    result = weeks_needed
    return result

print(solution())