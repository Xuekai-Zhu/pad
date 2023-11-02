def solution():
    # Calculate the total income in June
    milk_per_month = 200 * 30  # cows produce 200 gallons of milk every day, so they produce 200*30 gallons in a month
    income_per_gallon = 3.55  # Mr. Jesiah sells 1 gallon of milk for $3.55
    total_income = milk_per_month * income_per_gallon - 3000  # total income in June is the total milk sales minus expenses
    result = total_income
    return result

print(solution())