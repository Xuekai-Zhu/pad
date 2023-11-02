def solution():
    # Calculate the number of customers in each week
    week1_customers = 35
    week2_customers = 2 * week1_customers
    week3_customers = 3 * week1_customers

    # Calculate the total commission earned for all weeks
    total_commission = week1_customers + week2_customers + week3_customers

    # Calculate the total earnings including salary and bonus
    total_earnings = total_commission + 500 + 50
    result = total_earnings
    return result

print(solution())