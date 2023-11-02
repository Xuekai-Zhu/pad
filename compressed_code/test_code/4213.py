def solution():
    
    rent = 600
    food = (3/5) * rent
    mortgage = 3 * food
    savings = 2000
    taxes = (2/5) * savings
    total_expenses = rent + food + mortgage + taxes
    gross_salary = total_expenses + savings
    result = gross_salary
    return result

print(solution())