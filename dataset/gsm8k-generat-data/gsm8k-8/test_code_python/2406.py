def solution():
    # Calculate the total number of bedrooms and bathrooms
    total_bedrooms_and_bathrooms = 3 * (12 + 7)

    # Subtract the number of bedrooms and bathrooms from the total rooms to get the number of kitchens
    total_kitchens = 72 - total_bedrooms_and_bathrooms

    result = total_kitchens
    return result

print(solution())