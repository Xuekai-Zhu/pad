def solution():
    # Calculate the total length of TV James watched in minutes
    total_minutes = (2 * 20) + (2 * 2 * 20)  # James watched 2 episodes of Jeopardy and 2 episodes of Wheel of Fortune, with the latter being twice as long
    # Convert total minutes to hours
    total_hours = total_minutes / 60
    result = total_hours
    return result

print(solution())