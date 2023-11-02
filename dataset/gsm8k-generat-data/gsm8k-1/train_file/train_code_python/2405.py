def solution():
    """The space station, Lupus-1, is an enormous spacecraft made up of three identical cylindrical structures that house the living quarters for the crew. The three cylindrical structures are linked together by a series of tunnels that hold them together and allow the crew to move between cylinders. Each cylindrical structure contains 12 bedrooms, 7 bathrooms, and several kitchens. If the entire space station has 72 rooms, how many kitchens are there on the entire space station?"""
    total_rooms = 72
    rooms_per_cylinder = 12 + 7 + x # x is the number of kitchens
    cylinders = 3
    total_kitchens = (total_rooms - cylinders * (12 + 7)) / cylinders
    result = total_kitchens
    
    return result

print(solution())