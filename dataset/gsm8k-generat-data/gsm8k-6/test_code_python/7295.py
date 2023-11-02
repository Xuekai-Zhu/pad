def solution():
    # Calculate the square miles of the region east of plain A
    region_A = 200 - 50  # given that the region east of A is 50 square miles less than the region east of B

    # Calculate the total square miles of both plains
    total_square_miles = region_A + 200  # given that plain B has 200 square miles

    result = total_square_miles
    return result

print(solution())