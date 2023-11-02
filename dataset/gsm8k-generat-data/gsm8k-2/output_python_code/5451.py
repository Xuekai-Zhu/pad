def solution():
    """On a monthly basis, Esperanza pays $600 in rent, 3/5 as much money on food as she pays on rent and her mortgage bill costs three times the amount of money she spends on food. If she saves $2000 and also pays the equivalent of 2/5 of her savings in taxes, calculate her gross monthly salary."""
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