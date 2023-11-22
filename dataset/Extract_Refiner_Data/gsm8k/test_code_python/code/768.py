def solution():
    
    # Define the number of hours Tatiana has on each day
    saturday_hours = 7
    sunday_hours = 5

    # Calculate the total number of hours Tatiana has
    total_hours = saturday_hours + sunday_hours

    # Subtract the hours Tatiana spends reading
    remaining_hours = total_hours - 3

    # Calculate the number of hours Tatiana spends playing video games
    video_game_hours = remaining_hours / 3

    # Subtract the hours Tatiana spends playing video games
    remaining_hours -= video_game_hours

    # Calculate the percentage of Tatiana's weekend spent playing soccer
    soccer_percentage = (soccer_hours / remaining_hours) * 100

    # Display the percentage of Tatiana's weekend spent playing soccer
    result = soccer_percentage
    return result

print(solution())