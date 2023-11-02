def solution():
    """Leila and her friends want to rent a car for their one-day trip that is 150 kilometers long each way. 
    The first option for a car rental costs $50 a day, excluding gasoline. 
    The second option costs $90 a day including gasoline. 
    A liter of gasoline can cover 15 kilometers and costs $0.90 per liter. 
    Their car rental will need to carry them to and from their destination. 
    How much will they save if they will choose the first option rather than the second one?"""
    distance = 150 * 2  # round trip
    gas_price_per_liter = 0.9
    gas_km_per_liter = 15
    gas_needed = distance / gas_km_per_liter
    gas_price_total = gas_price_per_liter * gas_needed
    option1_price = 50 + gas_price_total
    option2_price = 90
    savings = option2_price - option1_price
    result = savings
    return result

print(solution())