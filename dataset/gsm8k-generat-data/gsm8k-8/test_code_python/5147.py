def solution():
    hourly_wage = 12.00 # Rachel's hourly wage
    num_customers = 20 # Number of customers served in one hour
    tip_per_customer = 1.25 # Tip left per customer

    total_tip = num_customers * tip_per_customer # Calculating total tip earned
    hourly_earnings = hourly_wage + total_tip # Adding hourly wage and tips to get total earnings

    result = hourly_earnings # Assigning result to variable and returning it
    return result

print(solution())