def solution():
    """Tara's taking a road trip for the weekend. She drives for two days, stopping to fill up her gas tank each time from empty to full when she needs it. She visits 4 different gas stations in total, with the price of gas being $3, $3.50, $4, and $4.50 respectively at each. If Tara's car has a 12-gallon tank, how much does she spend on gas for her road trip?"""
    gas_prices = [3, 3.5, 4, 4.5]
    total_gallons = 24  # 12-gallon tank filled twice
    total_cost = 0
    for i in range(4):
        gallons = 12
        cost = gallons * gas_prices[i]
        total_cost += cost
    result = total_cost
    return result

print(solution())