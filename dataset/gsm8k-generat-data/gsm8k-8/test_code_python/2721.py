def solution():
    # Calculate the number of sticks Felicity collects each week
    sticks_per_week = 3 * 1  # since she always goes and gets one lollipop per trip

    # Calculate the total number of sticks Felicity has collected so far
    total_sticks = (100/60) * 400  # since the fort is 60% complete

    # Calculate the number of weeks Felicity has been collecting sticks for
    weeks = total_sticks / sticks_per_week

    result = weeks
    return result

print(solution())