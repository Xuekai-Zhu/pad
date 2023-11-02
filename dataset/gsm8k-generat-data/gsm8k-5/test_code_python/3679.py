def solution():
    total_cost = 3  # The shirt costs $3
    saved_amount = 1.5  # Macey has already saved $1.50
    remaining_amount = total_cost - saved_amount  # Macey needs to save the remaining amount
    saving_per_week = 0.5  # Macey saves $0.50 per week

    # Calculate the number of weeks Macey needs to save for the remaining amount
    weeks_needed = remaining_amount / saving_per_week
    result = weeks_needed
    return result

print(solution())