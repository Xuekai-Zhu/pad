def solution():
    
    # Define the number of pieces added per minute by Kalinda and her mom
    pieces_per_minute = 4 / 2

    # Calculate the total number of pieces added per minute by both Kalinda and her mom
    total_pieces_per_minute = pieces_per_minute * 360

    # Calculate the total time it will take to complete the puzzle in minutes
    total_time_in_minutes = total_pieces_per_minute / 60

    # Convert the total time to hours
    total_time_in_hours = total_time_in_minutes / 60

    # Display the total time in hours
    result = total_time_in_hours
    return result

print(solution())