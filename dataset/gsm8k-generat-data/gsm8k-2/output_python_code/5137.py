def solution():
    """A hotel has 10 rooms and is currently full. Each room holds a family of 3. If each person receives 2 towels, how many towels does the hotel hand out?"""
    num_rooms = 10
    num_people_per_room = 3
    num_towels_per_person = 2
    num_towels = num_rooms * num_people_per_room * num_towels_per_person
    result = num_towels
    return result

print(solution())