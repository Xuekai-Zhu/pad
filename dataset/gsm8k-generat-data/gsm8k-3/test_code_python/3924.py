def solution():
    """Luisa drives 10 miles to the grocery store, 6 miles to the mall, 5 miles to the pet store, then 9 miles back home. One gallon of gas can be used to drive 15 miles. If one gallon of gas costs $3.50, what is the total cost of the gas for Luisa’s entire trip?"""
    # Calculate the total distance that Luisa travels
    total_distance = 10 + 6 + 5 + 9

    # Calculate the number of gallons of gas needed
    gallons_needed = total_distance / 15

    # Calculate the total cost of the gas
    gas_cost = gallons_needed * 3.50

    # Display the total cost of the gas
    result = gas_cost
    return result

print(solution())