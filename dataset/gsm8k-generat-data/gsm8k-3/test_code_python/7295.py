def solution():
    """The region east of plain A is 50 square miles less than the region east of plain B. If plain B has 200 square miles, how many square miles do the plains have in total?"""
    # Determine the area east of plains A
    area_A = area_B - 50

    # Determine the total area of the plains
    total_area = area_A + area_B

    # Display the total area of the plains
    result = total_area
    return result

print(solution())