def solution():
    rent = 600
    food = (3/5) * rent
    mortgage = 3 * food
    savings = 2000
    tax = (2/5) * savings
    
    # Calculate total expenses
    expenses = rent + food + mortgage + tax
    
    # Calculate gross monthly salary
    gross_salary = expenses + savings
    
    result = gross_salary
    return result

print(solution())