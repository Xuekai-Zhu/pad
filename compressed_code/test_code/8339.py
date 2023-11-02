def solution():
    
    total_area = 1110
    bedrooms_area = 4 * (11 * 11)
    bathrooms_area = 2 * (6 * 8)
    kitchen_living_area = total_area - bedrooms_area - bathrooms_area
    kitchen_area = kitchen_living_area / 2 
    result = kitchen_area
    return result

print(solution())