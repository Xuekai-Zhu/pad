def solution():
    num_blue_shirts = 26
    num_brown_shirts = 36

    # Calculate the number of blue shirts Mary gives away
    num_blue_give_away = num_blue_shirts / 2

    # Calculate the number of brown shirts Mary gives away
    num_brown_give_away = num_brown_shirts / 3

    # Calculate the total number of shirts Mary has left
    total_shirts_left = num_blue_shirts - num_blue_give_away + num_brown_shirts - num_brown_give_away

    result = total_shirts_left
    return result

print(solution())