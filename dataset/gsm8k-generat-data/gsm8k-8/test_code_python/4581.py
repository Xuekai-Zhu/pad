def solution():
    # Define the amount of milk produced in June
    milk_production = 200 * 30

    # Calculate the income from selling the milk
    milk_income = milk_production * 3.55

    # Calculate the total income by subtracting expenses from milk income
    total_income = milk_income - 3000
    result = total_income
    return result

print(solution())