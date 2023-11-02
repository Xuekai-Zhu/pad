def solution():
    # Calculate the total distance the flag moved up and down the pole
    distance_moved = 60  # the flag starts at the top of the pole
    distance_moved += (60/2)  # the flag is lowered halfway down the pole
    distance_moved += 60  # the flag is raised back up to the top of the pole
    distance_moved += (60/2)  # the flag is then lowered all the way down and taken off the pole
    result = distance_moved
    return result

print(solution())