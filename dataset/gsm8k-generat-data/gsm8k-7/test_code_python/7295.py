def solution():
    region_a = region_b - 50  # region east of plain A is 50 sq miles less than region east of B
    region_b = 200  # given that plain B has 200 sq miles

    # Calculate the total square miles of both plains
    total_square_miles = region_a + region_b
    result = total_square_miles
    return result

print(solution())