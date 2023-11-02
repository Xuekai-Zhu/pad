def solution():
    """Mr. Jesiah is a dairy cow farmer with cows producing 200 gallons of milk every day. The expenses for maintenance of the dairy farm and purchase of feeds is $3000 per month. Calculate his total income in June if he sells 1 gallon of milk at $3.55."""
    milk_production = 200 * 30 # assuming 30 days in June
    milk_price = 3.55
    income = milk_production * milk_price
    expenses = 3000
    total_income = income - expenses
    result = total_income
    return result

print(solution())