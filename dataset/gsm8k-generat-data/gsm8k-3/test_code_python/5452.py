def solution():
    """On a monthly basis, Esperanza pays $600 in rent, 3/5 as much money on food as she pays on rent and her mortgage bill costs three times the amount of money she spends on food. If she saves $2000 and also pays the equivalent of 2/5 of her savings in taxes, calculate her gross monthly salary."""
    # Calculate the amount of money Esperanza spends on food
    food_spending = (3/5) * 600

    # Calculate the amount of money Esperanza pays on her mortgage
    mortgage_bill = 3 * food_spending

    # Calculate the total amount of money Esperanza spends on all bills
    total_bills = 600 + food_spending + mortgage_bill

    # Subtract the amount Esperanza saves and pays in taxes from her total spending to get her gross monthly salary
    gross_salary = total_bills + 2000 + (2/5) * 2000

    # Display Esperanza's gross salary
    result = gross_salary
    return result

print(solution())