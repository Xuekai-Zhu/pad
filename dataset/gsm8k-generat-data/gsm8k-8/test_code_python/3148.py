def solution():
    # Define variables
    pants_shirt_cost = 100
    pants_coat_cost = 244
    coat_shirt_ratio = 5

    # Solve for shirt cost
    shirt_cost = pants_shirt_cost - 2  # Subtracting the pants cost from total

    # Solve for coat cost
    coat_cost = coat_shirt_ratio * shirt_cost

    result = coat_cost
    return result

print(solution())