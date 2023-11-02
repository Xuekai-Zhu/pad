def solution():
    """Leila and her friends want to rent a car for their one-day trip that is 150 kilometers long each way. 
    The first option for a car rental costs $50 a day, excluding gasoline. 
    The second option costs $90 a day including gasoline. 
    A liter of gasoline can cover 15 kilometers and costs $0.90 per liter. 
    Their car rental will need to carry them to and from their destination. 
    How much will they save if they will choose the first option rather than the second one?"""
    distance = 150 * 2  # round trip distance
    gas_price_per_liter = 0.9
    gas_coverage_per_liter = 15
    liters_needed = distance / gas_coverage_per_liter
    gas_cost = liters_needed * gas_price_per_liter
    first_rental_cost = 50
    second_rental_cost = 90
    total_cost_first_option = first_rental_cost + gas_cost
    total_cost_second_option = second_rental_cost
    savings = total_cost_second_option - total_cost_first_option
    return savings

print(solution())