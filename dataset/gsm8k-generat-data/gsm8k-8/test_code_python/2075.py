def solution():
    # Define the length of the hallway and the ratio of speeds between the father and son
    length = 16
    ratio = 3

    # Calculate the total distance covered by the father and son before they meet
    total_distance = length / (1 + ratio)

    # Calculate the distance from the father's end of the hallway where they will meet
    distance_from_father = ratio * total_distance

    result = distance_from_father
    return result

print(solution())