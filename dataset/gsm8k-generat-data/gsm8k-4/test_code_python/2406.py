def solution():
    """The space station, Lupus-1, is an enormous spacecraft made up of three identical cylindrical structures that house the living quarters for the crew. The three cylindrical structures are linked together by a series of tunnels that hold them together and allow the crew to move between cylinders. Each cylindrical structure contains 12 bedrooms, 7 bathrooms, and several kitchens. If the entire space station has 72 rooms, how many kitchens are there on the entire space station?"""
    # Define the number of bedrooms and bathrooms per cylindrical structure
    bedrooms_per_cylinder = 12
    bathrooms_per_cylinder = 7

    # Define the total number of rooms in the entire space station
    total_rooms = 72

    # Calculate the number of rooms per cylindrical structure
    rooms_per_cylinder = total_rooms / 3

    # Calculate the number of kitchens per cylindrical structure based on the number of rooms per cylinder
    kitchens_per_cylinder = rooms_per_cylinder - bedrooms_per_cylinder - bathrooms_per_cylinder

    # Calculate the total number of kitchens on the entire space station
    total_kitchens = kitchens_per_cylinder * 3

    result = total_kitchens
    return result

print(solution())