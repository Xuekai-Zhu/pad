def solution():
    weekly_savings = 25
    num_weeks = 8
    
    # Calculate the total amount of money saved before using any money for bills or the coat
    total_savings = weekly_savings * num_weeks
    
    # Calculate the amount of money used to pay bills
    bills_cost = total_savings / 3
    total_savings -= bills_cost
    
    # Calculate the remaining amount of money needed to buy the coat
    coat_cost = 170
    remaining_cost = coat_cost - total_savings
    
    # Calculate the amount of money his dad gave him
    dad_money = remaining_cost
    
    result = dad_money
    return result

print(solution())