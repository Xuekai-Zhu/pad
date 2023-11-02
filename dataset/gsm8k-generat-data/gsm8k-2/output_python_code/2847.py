def solution():
    """Jason and Jeremy want to paint their wall white and agreed to split the cost of the paint. A gallon of paint costs $45 and can cover up to 400 square feet. How much will each of them contribute to the cost of the paint if their walls have a total area of 1600 square feet and will need a second coat?"""
    total_area = 1600
    gallons_needed = (total_area / 400) * 2
    cost_per_person = (gallons_needed * 45) / 2
    result = cost_per_person
    return result

print(solution())