def solution():
    # Calculate the number of pencils Jenine needs
    pencils_needed = int((105 / 1.5) / 5) + 1  # add 1 to account for the first pencil

    # Calculate the cost of the pencils Jenine needs
    cost_of_pencils = pencils_needed * 2

    result = cost_of_pencils
    return result

print(solution())