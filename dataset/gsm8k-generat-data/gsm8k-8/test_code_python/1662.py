def solution():
    # Define the initial number of tomatoes
    initial_tomatoes = 100

    # Calculate the number of tomatoes Jane picks in the first week
    first_week_pick = initial_tomatoes * 1/4

    # Calculate the total number of tomatoes remaining after the first week
    remaining_tomatoes = initial_tomatoes - first_week_pick

    # Calculate the number of tomatoes Jane picks in the second week
    second_week_pick = 20

    # Calculate the total number of tomatoes remaining after the second week
    remaining_tomatoes -= second_week_pick

    # Calculate the number of tomatoes Jane picks in the third week
    third_week_pick = second_week_pick * 2

    # Calculate the total number of tomatoes remaining after the third week
    remaining_tomatoes -= third_week_pick

    result = remaining_tomatoes
    return result

print(solution())