def solution():
    num_pencils = 30
    lost_pencils_1 = 6
    lost_pencils_2 = (num_pencils - lost_pencils_1) / 3

    # Calculate the number of pencils Charley currently has
    num_pencils_left = num_pencils - lost_pencils_1 - lost_pencils_2

    result = num_pencils_left
    return result

print(solution())