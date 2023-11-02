def solution():
    """Jason and Jeremy want to paint their wall white and agreed to split the cost of the paint. A gallon of paint costs $45 and can cover up to 400 square feet. How much will each of them contribute to the cost of the paint if their walls have a total area of 1600 square feet and will need a second coat?"""
    # Define the area of their walls and the cost per gallon of paint
    wall_area = 1600
    gallon_cost = 45

    # Calculate the number of gallons needed to cover the walls twice
    gallons_needed = (wall_area * 2) / 400

    # Calculate the total cost of the paint
    total_cost = gallons_needed * gallon_cost

    # Calculate the cost per person
    cost_per_person = total_cost / 2

    # Return the result
    result = cost_per_person
    return result

print(solution())