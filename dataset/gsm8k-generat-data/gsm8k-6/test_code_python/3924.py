def solution():
    # Calculate the total distance Luisa drove
    total_distance = 10 + 6 + 5 + 9

    # Calculate the total number of gallons of gas Luisa used
    gallons_used = total_distance // 15 + 1  # Round up to the nearest gallon

    # Calculate the total cost of the gas
    total_cost = gallons_used * 3.5
    result = total_cost
    return result

print(solution())