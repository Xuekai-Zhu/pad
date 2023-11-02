def solution():
    """Luisa drives 10 miles to the grocery store, 6 miles to the mall, 5 miles to the pet store, then 9 miles back home. One gallon of gas can be used to drive 15 miles. If one gallon of gas costs $3.50, what is the total cost of the gas for Luisa’s entire trip?"""
    total_miles = 10 + 6 + 5 + 9
    miles_per_gallon = 15
    gallons_needed = total_miles / miles_per_gallon
    cost_per_gallon = 3.5
    total_cost = gallons_needed * cost_per_gallon
    result = total_cost
    return result

print(solution())