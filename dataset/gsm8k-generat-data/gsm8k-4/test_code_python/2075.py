def solution():
    """A father and a son start approaching each other at the same time from opposite ends of a hallway that is 16m long. If the father is walking three times as fast as the son, at what distance from the father's end of the hallway will they meet?"""
    # Define the length of the hallway and the speeds of the father and son
    hallway_length = 16
    father_speed = 3
    son_speed = 1

    # Calculate the total speed of the father and son
    total_speed = father_speed + son_speed

    # Calculate the time it takes for them to meet
    time_to_meet = hallway_length / total_speed

    # Calculate the distance from the father's end of the hallway
    distance_from_father_end = father_speed * time_to_meet

    # return the result
    result = distance_from_father_end
    return result

print(solution())