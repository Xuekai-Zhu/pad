def solution():
    # Calculate the total amount of expenses for the household
    total_expenses = 42 + taxes
    
    # Calculate Angie's total income for the month
    total_income = 80
    
    # Calculate Angie's total expenses for the month
    total_angie_expenses = total_expenses + total_income
    
    # Calculate the amount of taxes Angie paid this month
    taxes = total_angie_expenses - 18 - total_income
    
    result = taxes
    return result

print(solution())