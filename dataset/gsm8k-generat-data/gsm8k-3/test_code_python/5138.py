def solution():
    """A hotel has 10 rooms and is currently full. Each room holds a family of 3. If each person receives 2 towels, how many towels does the hotel hand out?"""
    # Define the number of rooms and the number of people in each room
    num_rooms = 10
    num_people_per_room = 3

    # Calculate the total number of people in the hotel
    total_people = num_rooms * num_people_per_room

    # Calculate the total number of towels handed out
    total_towels = total_people * 2

    # Display the total number of towels
    result = total_towels
    return result

print(solution())