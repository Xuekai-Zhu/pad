def solution():
    # Calculate the total number of bedrooms and bathrooms on the space station
    total_bedrooms = 12 * 3  # 3 cylindrical structures each containing 12 bedrooms
    total_bathrooms = 7 * 3  # 3 cylindrical structures each containing 7 bathrooms
    total_rooms = total_bedrooms + total_bathrooms  # total number of bedrooms and bathrooms

    # Calculate the total number of kitchens on the space station
    total_kitchens = 72 - total_rooms  # the remaining rooms are kitchens
    result = total_kitchens
    return result

print(solution())