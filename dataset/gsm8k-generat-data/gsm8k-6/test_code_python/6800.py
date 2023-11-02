def solution():
    # Calculate the number of pencils Autumn had left after the first month of school
    initial_pencils = 20
    lost_pencils = 7
    broken_pencils = 3
    found_pencils = 4
    bought_pencils = 2
    pencils_left = initial_pencils - lost_pencils - broken_pencils + found_pencils + bought_pencils
    result = pencils_left
    return result

print(solution())