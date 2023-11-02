def solution():
    # Calculate the total area to be covered
    total_area = 1600 * 2

    # Calculate how many gallons of paint they need
    gallons_of_paint = total_area / 400

    # Calculate the total cost of the paint
    total_cost = gallons_of_paint * 45

    # Calculate how much each person will contribute to the cost
    cost_per_person = total_cost / 2

    result = cost_per_person
    return result

print(solution())