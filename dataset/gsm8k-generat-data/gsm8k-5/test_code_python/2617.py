def solution():
    total_area = 16 * 10  # Calculate the total area of the apartment
    num_of_same_size_rooms = 6 - 1  # There are 6 rooms in total and 1 is the living room, so there are 5 same-sized rooms
    area_of_same_size_rooms = total_area / num_of_same_size_rooms  # Divide the total area by the number of same-sized rooms to get the area of one room
    area_of_living_room = 3 * area_of_same_size_rooms  # The living room is 3 times the size of one of the same-sized rooms
    result = area_of_living_room
    return result

print(solution())