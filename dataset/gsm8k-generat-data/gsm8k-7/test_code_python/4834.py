def solution():
    rung_length = 18 / 12  # convert inches to feet
    distance_between_rungs = 6 / 12  # convert inches to feet
    height_of_tree = 50
    num_rungs = (height_of_tree * 12) / distance_between_rungs  # convert feet to inches
    length_of_wood = num_rungs * rung_length
    result = length_of_wood
    return result

print(solution())