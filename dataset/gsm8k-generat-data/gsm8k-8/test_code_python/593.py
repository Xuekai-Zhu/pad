def solution():
    # Define the final depth of the snowdrift
    final_depth = 34

    # Calculate the depth of the snowdrift after the third day
    third_day_depth = final_depth - 18 - 6

    # Calculate the depth of the snowdrift after the second day
    second_day_depth = third_day_depth * 2

    # Calculate the depth of the snowdrift after the first day
    first_day_depth = second_day_depth + third_day_depth

    result = first_day_depth
    return result

print(solution())