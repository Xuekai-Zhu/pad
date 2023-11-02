def solution():
    """Luisa drives 10 miles to the grocery store, 6 miles to the mall, 5 miles to the pet store, then 9 miles back home. One gallon of gas can be used to drive 15 miles. If one gallon of gas costs $3.50, what is the total cost of the gas for Luisa’s entire trip?"""
    total_distance = 10 + 6 + 5 + 9
    gallon_per_mile = 1 / 15
    total_gallon_needed = total_distance * gallon_per_mile
    cost_per_gallon = 3.50
    total_cost = total_gallon_needed * cost_per_gallon
    result = total_cost
    return result

print(solution())