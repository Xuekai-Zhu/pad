def solution():
    first_level = 4
    second_level = first_level + 7
    third_level = second_level + 6
    fourth_level = 14

    # Calculate the total number of open parking spots
    total_spots = first_level + second_level + third_level + fourth_level
    result = total_spots
    return result

print(solution())