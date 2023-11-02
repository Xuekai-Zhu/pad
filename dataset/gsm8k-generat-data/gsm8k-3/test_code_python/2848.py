def solution():
    """Jason and Jeremy want to paint their wall white and agreed to split the cost of the paint. A gallon of paint costs $45 and can cover up to 400 square feet. How much will each of them contribute to the cost of the paint if their walls have a total area of 1600 square feet and will need a second coat?"""
    
    # Define the area to be covered and the coverage per gallon of paint
    area = 1600 * 2
    coverage_per_gallon = 400

    # Calculate the number of gallons of paint needed
    gallons_needed = area / coverage_per_gallon

    # Calculate the total cost of the paint
    total_cost = gallons_needed * 45

    # Calculate the cost per person
    cost_per_person = total_cost / 2

    # Display the cost per person
    result = cost_per_person
    return result

print(solution())