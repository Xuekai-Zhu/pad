def solution():
    initial_investment = 300  # initial investment
    monthly_interest = 0.1  # 10% interest at the end of each month
    
    # Calculate total investment at the end of 2 months
    total_investment = initial_investment + (initial_investment * monthly_interest) + ((initial_investment + (initial_investment * monthly_interest)) * monthly_interest)
    
    result = total_investment
    return result

print(solution())