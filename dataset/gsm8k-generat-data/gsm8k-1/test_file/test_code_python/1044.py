def solution():
    """Ben bought a car for $20000 in 2007. The price of the car depreciates at a constant rate of 21% per year. Find the price of the car in the year 2010."""
    initial_price = 20000
    depreciation_rate = 0.21
    years_passed = 3
    final_price = initial_price * (1 - depreciation_rate) ** years_passed
    result = final_price
    return result

print(solution())