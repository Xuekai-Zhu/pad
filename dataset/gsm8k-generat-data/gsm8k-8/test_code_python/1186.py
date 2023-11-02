def solution():
    # Calculate the cost of permits
    permit_cost = 250

    # Calculate the cost of contractor
    contractor_cost = 150 * 3 * 5

    # Calculate the inspector's cost
    inspector_cost = contractor_cost * 0.8

    # Calculate the total cost
    total_cost = permit_cost + contractor_cost + inspector_cost
    result = total_cost
    return result

print(solution())