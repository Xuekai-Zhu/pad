def solution():
    total_rooms = 72
    rooms_per_cylinder = 12 + 7
    num_cylinders = total_rooms / rooms_per_cylinder
    num_kitchens = num_cylinders * 1
    result = num_kitchens
    return num_kitchens

print(solution())