def solution():
    """The region east of plain A is 50 square miles less than the region east of plain B. If plain B has 200 square miles, how many square miles do the plains have in total?"""
    # Define the area of plain B and calculate the area of plain A
    area_b = 200
    area_a = area_b - 50
    
    # Calculate the total area of the plains
    total_area = area_a + area_b
    
    # Return the result
    result = total_area
    return result

print(solution())