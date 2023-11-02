def solution():
    """Bobby received his weekly paycheck today. Although his salary is $450 per week, his actual paycheck is reduced in size
    because there are some taxes, insurance payments, and fees removed from his pay before his employer writes the check. If the government
    removes 1/3 in federal taxes and 8% in state taxes, the health insurance removes $50 per week, the life insurance removes $20 per week,
    and the city charges him a fee of $10 per week for parking, then what is the final amount left in Bobby's paycheck, in dollars?"""
    
    # Define the initial salary and the percentage of taxes
    salary = 450
    federal_taxes_percentage = 1/3
    state_taxes_percentage = 0.08
    
    # Calculate the total amount removed due to taxes
    total_taxes = salary * (federal_taxes_percentage + state_taxes_percentage)
    
    # Subtract the taxes and insurance payments from the initial salary
    net_income = salary - total_taxes - 50 - 20 - 10
    
    # Return the final amount in Bobby's paycheck
    return net_income

print(solution())