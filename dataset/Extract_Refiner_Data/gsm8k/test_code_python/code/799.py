def solution():
    
    # Define the total number of hours Kris needs to play
    total_hours = 30

    # Calculate the number of hours Kris plays in the first 2 weeks
    hours_played_first_week = 0.5 * 7 * 2

    # Calculate the number of hours Kris plays in the next 2 weeks
    hours_played_second_week = 2 * 7 * 2

    # Calculate the total number of hours Kris has played so far
    total_hours_played = hours_played_first_week + hours_played_second_week

    # Calculate the number of hours Kris still needs to play to earn the achievement
    hours_left_to_play = total_hours - total_hours_played

    # Display the number of hours Kris still needs to play
    result = hours_left_to_play
    return result

print(solution())