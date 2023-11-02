def solution():
    """The space station, Lupus-1, is an enormous spacecraft made up of three identical cylindrical structures that house the living quarters for the crew. The three cylindrical structures are linked together by a series of tunnels that hold them together and allow the crew to move between cylinders. Each cylindrical structure contains 12 bedrooms, 7 bathrooms, and several kitchens. If the entire space station has 72 rooms, how many kitchens are there on the entire space station?"""
    bedrooms_per_cylinder = 12
    bathrooms_per_cylinder = 7
    total_rooms_per_cylinder = bedrooms_per_cylinder + bathrooms_per_cylinder + x
    total_rooms = 72
    total_cylinders = 3
    kitchens_per_cylinder = total_rooms_per_cylinder - bedrooms_per_cylinder - bathrooms_per_cylinder
    total_kitchens = kitchens_per_cylinder * total_cylinders
    result = total_kitchens
    return result

print(solution())