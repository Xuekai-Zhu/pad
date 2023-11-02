def solution():
    """The space station, Lupus-1, is an enormous spacecraft made up of three identical cylindrical structures that house the living quarters for the crew.   The three cylindrical structures are linked together by a series of tunnels that hold them together and allow the crew to move between cylinders.  Each cylindrical structure contains 12 bedrooms, 7 bathrooms, and several kitchens.  If the entire space station has 72 rooms, how many kitchens are there on the entire space station?"""
    # Define the number of bedrooms and bathrooms in each cylindrical structure
    BEDROOMS = 12
    BATHROOMS = 7

    # Calculate the total number of rooms in each cylindrical structure
    rooms_per_cylinder = BEDROOMS + BATHROOMS

    # Calculate the total number of rooms in the entire space station
    total_rooms = rooms_per_cylinder * 3

    # Calculate the number of kitchens in the entire space station
    kitchens = 72 - total_rooms

    # Display the number of kitchens
    result = kitchens
    return result

print(solution())