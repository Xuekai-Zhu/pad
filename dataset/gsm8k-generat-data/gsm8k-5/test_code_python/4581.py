def solution():
    milk_production_per_month = 200 * 30  # Cows produce 200 gallons of milk every day, and there are 30 days in a month
    cost_of_maintenance_and_feed = 3000  # The monthly expenses for maintenance and feed is $3000
    price_per_gallon = 3.55  # Mr. Jesiah sells 1 gallon of milk at $3.55

    # Calculate the total income from milk sales
    total_income = milk_production_per_month * price_per_gallon

    # Calculate the profit after deducting expenses
    total_profit = total_income - cost_of_maintenance_and_feed
    result = total_profit
    return result

print(solution())