def solution():
    # Calculate Jack's points
    jon_points = 3
    jack_points = jon_points + 5

    # Calculate Tom's points
    tom_points = jon_points + jack_points - 4

    # Calculate the total points scored by all three
    total_points = jon_points + jack_points + tom_points
    result = total_points
    return result

print(solution())