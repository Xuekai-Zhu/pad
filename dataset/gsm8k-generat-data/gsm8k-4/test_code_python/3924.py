def solution():
    """Luisa drives 10 miles to the grocery store, 6 miles to the mall, 5 miles to the pet store, then 9 miles back home. One gallon of gas can be used to drive 15 miles. If one gallon of gas costs $3.50, what is the total cost of the gas for Luisa’s entire trip?"""
    # Calculate the total distance of the trip
    total_distance = 10 + 6 + 5 + 9

    # Calculate the total number of gallons needed for the trip
    total_gallons = total_distance / 15

    # Calculate the total cost of the gas
    total_cost = total_gallons * 3.5

    # return the result
    result = round(total_cost, 2)
    return result

print(solution())