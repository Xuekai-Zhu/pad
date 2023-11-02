def solution():
    num_rooms = 10
    room_capacity = 3
    towels_per_person = 2

    # Calculate the total number of people in the hotel
    total_people = num_rooms * room_capacity

    # Calculate the total number of towels that the hotel hands out
    total_towels = total_people * towels_per_person
    result = total_towels
    return result

print(solution())