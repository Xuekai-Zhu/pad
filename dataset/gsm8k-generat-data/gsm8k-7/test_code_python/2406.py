def solution():
    num_cylinders = 3
    num_bedrooms_per_cylinder = 12
    num_bathrooms_per_cylinder = 7
    total_rooms = 72

    # Calculate the total number of bedrooms on the entire space station
    total_bedrooms = num_cylinders * num_bedrooms_per_cylinder

    # Calculate the total number of bathrooms on the entire space station
    total_bathrooms = num_cylinders * num_bathrooms_per_cylinder

    # Calculate the total number of kitchens on the entire space station
    total_kitchens = total_rooms - total_bedrooms - total_bathrooms
    result = total_kitchens
    return result

print(solution())