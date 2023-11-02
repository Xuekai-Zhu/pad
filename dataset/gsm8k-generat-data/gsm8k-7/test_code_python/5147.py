def solution():
    hourly_wage = 12.0
    num_customers = 20
    tip_per_customer = 1.25

    # Calculate total amount of tips Rachel earned
    total_tips = num_customers * tip_per_customer

    # Calculate total amount of money Rachel earned in the hour
    total_earned = hourly_wage + total_tips
    result = total_earned
    return result

print(solution())