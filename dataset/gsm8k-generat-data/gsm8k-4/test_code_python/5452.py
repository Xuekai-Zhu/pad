def solution():
    """On a monthly basis, Esperanza pays $600 in rent, 3/5 as much money on food as she pays on rent and her mortgage bill costs three times the amount of money she spends on food. If she saves $2000 and also pays the equivalent of 2/5 of her savings in taxes, calculate her gross monthly salary."""
    # Define the cost of rent
    rent = 600

    # Calculate the cost of food
    food = (3/5) * rent

    # Calculate the cost of the mortgage bill
    mortgage = 3 * food

    # Calculate the total monthly expenses
    expenses = rent + food + mortgage

    # Calculate the amount of taxes paid
    taxes = (2/5) * 2000

    # Calculate the gross monthly salary
    salary = expenses + taxes + 2000

    result = salary
    return result

print(solution())