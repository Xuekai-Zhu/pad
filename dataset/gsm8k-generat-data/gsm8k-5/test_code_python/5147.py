def solution():
    hourly_wage = 12.00  # Rachel makes $12.00 per hour
    num_customers = 20  # Rachel serves 20 different people in one hour
    tip_per_customer = 1.25  # Each customer leaves a $1.25 tip

    # Calculate the total amount Rachel made in tips
    total_tip = num_customers * tip_per_customer

    # Calculate Rachel's total earnings in one hour
    total_earnings = hourly_wage + total_tip
    result = total_earnings
    return result

print(solution())