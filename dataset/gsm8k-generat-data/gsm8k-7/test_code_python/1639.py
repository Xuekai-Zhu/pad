def solution():
    starting_balloons = 12
    ending_balloons = 50
    balloons_per_five_minutes = 2

    # Calculate the number of balloons Andy blew up
    balloons_blowed_by_andy = ending_balloons - starting_balloons

    # Calculate the number of five-minute increments Andy spent blowing up balloons
    time_increments = balloons_blowed_by_andy / balloons_per_five_minutes

    # Convert five-minute increments to minutes
    time_in_minutes = time_increments * 5
    result = time_in_minutes
    return result

print(solution())