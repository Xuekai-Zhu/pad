def solution():
    # Calculate the total number of points scored by Jon, Jack, and Tom
    jon_points = 3
    jack_points = jon_points + 5
    jon_jack_total = jon_points + jack_points
    tom_points = jon_jack_total - 4
    total_points = jon_points + jack_points + tom_points
    result = total_points
    return result

print(solution())