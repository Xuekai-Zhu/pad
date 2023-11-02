def solution():
    # Calculate the total number of boxes in Neighborhood A
    neighborhood_a = 10 * 2

    # Calculate the total number of boxes in Neighborhood B
    neighborhood_b = 5 * 5

    # Calculate the total amount from Neighborhood A
    total_a = neighborhood_a * 2

    # Calculate the total amount from Neighborhood B
    total_b = neighborhood_b * 2

    # Determine which neighborhood has the higher total amount
    if total_a > total_b:
        result = total_a
    else:
        result = total_b
    return result

print(solution())