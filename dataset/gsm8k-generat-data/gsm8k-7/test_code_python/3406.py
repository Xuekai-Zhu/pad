def solution():
    num_couples_rooms = 13
    num_single_rooms = 14
    bubble_bath_per_room = 10

    # Calculate the total amount of bubble bath needed for all couple's rooms
    bubble_bath_couples = num_couples_rooms * bubble_bath_per_room

    # Calculate the total amount of bubble bath needed for all single rooms
    bubble_bath_singles = num_single_rooms * bubble_bath_per_room

    # Calculate the total amount of bubble bath needed
    total_bubble_bath = bubble_bath_couples + bubble_bath_singles
    result = total_bubble_bath
    return result

print(solution())