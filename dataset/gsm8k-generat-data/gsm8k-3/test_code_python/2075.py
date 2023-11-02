def solution():
    """A father and a son start approaching each other at the same time from opposite ends of a hallway that is 16m long. If the father is walking three times as fast as the son, at what distance from the father's end of the hallway will they meet?"""
    # Define the length of the hallway and the speeds of the father and son
    hallway_length = 16
    father_speed = 3
    son_speed = 1

    # Calculate the time it takes for the father and son to meet
    total_speed = father_speed + son_speed
    time_to_meet = hallway_length / total_speed

    # Calculate the distance from the father's end of the hallway to the meeting point
    distance_from_father = father_speed * time_to_meet

    # Display the distance from the father's end of the hallway to the meeting point
    result = distance_from_father
    return result

print(solution())