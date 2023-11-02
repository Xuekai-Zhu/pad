def solution():
    """Mrs. Snyder used to spend 40% of her monthly income on rent and utilities. Her salary was recently increased by $600 so now her rent and utilities only amount to 25% of her monthly income. How much was her previous monthly income?"""
    
    # Define the current percentage spent on rent and utilities
    current_percentage = 0.25
    
    # Define the original percentage spent on rent and utilities
    original_percentage = 0.4
    
    # Define the increase in salary
    salary_increase = 600
    
    # Calculate the new total monthly income
    new_total_income = salary_increase / (current_percentage - original_percentage)
    
    # Calculate the previous monthly income
    previous_income = new_total_income / (1 + original_percentage)
    
    result = previous_income
    return result

print(solution())