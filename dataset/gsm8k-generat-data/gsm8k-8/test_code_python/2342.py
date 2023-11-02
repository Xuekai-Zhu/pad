def solution():
    # Define the monthly rate and the number of months
    monthly_rate = 50
    num_months = 4

    # Calculate the original total cost
    original_total_cost = monthly_rate * num_months

    # Calculate the discounted total cost if paid before the 25th day of the month
    discounted_total_cost = original_total_cost * 0.95

    # Calculate the final total cost if paid on the 25th day of the month for 4 months
    final_total_cost = discounted_total_cost * num_months

    result = final_total_cost
    return result

print(solution())