def solution():
    """Tara's taking a road trip for the weekend. She drives for two days, stopping to fill up her gas tank each time from empty to full when she needs it. She visits 4 different gas stations in total, with the price of gas being $3, $3.50, $4, and $4.50 respectively at each. If Tara's car has a 12-gallon tank, how much does she spend on gas for her road trip?"""
    tank_size = 12
    gas_stations = [(3, tank_size), (3.5, tank_size), (4, tank_size), (4.5, tank_size)]
    total_cost = 0
    for station in gas_stations:
        cost = station[0] * (station[1] / tank_size)
        total_cost += cost
    result = total_cost
    return result

print(solution())