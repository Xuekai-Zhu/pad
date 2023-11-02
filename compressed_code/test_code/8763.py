def solution():
    
    jon_points = 3
    jack_points = jon_points + 5
    jon_and_jack_points = jon_points + jack_points
    tom_points = jon_and_jack_points - 4
    total_points = jon_points + jack_points + tom_points
    result = total_points
    return result

print(solution())