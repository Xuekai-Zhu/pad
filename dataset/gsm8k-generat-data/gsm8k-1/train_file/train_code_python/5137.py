def solution():
    """A hotel has 10 rooms and is currently full. Each room holds a family of 3. If each person receives 2 towels, how many towels does the hotel hand out?"""
    num_rooms = 10
    occupants_per_room = 3
    towels_per_person = 2
    total_towels = num_rooms * occupants_per_room * towels_per_person
    result = total_towels
    return result

print(solution())