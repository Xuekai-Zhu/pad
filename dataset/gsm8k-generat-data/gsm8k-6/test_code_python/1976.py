def solution():
    # Calculate the number of boats left after fish and arrow attacks
    starting_boats = 30
    eaten_by_fish = 0.2 * starting_boats
    remaining_boats = starting_boats - eaten_by_fish - 2  # Madison shoots two of the boats
    result = remaining_boats
    return result

print(solution())