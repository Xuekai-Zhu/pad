def solution():
    # Calculate the number of customers in each week
    week1_customers = 35
    week2_customers = 2 * week1_customers
    week3_customers = 3 * week1_customers
    
    # Calculate the total commission Julio earns from each week
    week1_commission = week1_customers * 1
    week2_commission = week2_customers * 1
    week3_commission = week3_customers * 1
    
    # Calculate the total commission Julio earns for the 3 weeks
    total_commission = week1_commission + week2_commission + week3_commission
    
    # Calculate Julio's total earnings including salary and bonus
    total_earnings = total_commission + 500 + 50
    
    result = total_earnings
    return result

print(solution())