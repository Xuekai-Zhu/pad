def solution():
    kalinda_pieces = 360  # Kalinda is working on a 360 piece puzzle
    kalinda_speed = 4  # Kalinda can normally add 4 pieces per minute
    mom_speed = kalinda_pieces / 2  # Kalinda's mom can place half as many pieces per minute as Kalinda

    # Calculate the time it takes Kalinda to complete the puzzle
    time_kalinda = kalinda_pieces / kalinda_speed
    time_mom = mom_pieces / mom_speed
    total_time = time_kalinda + time_mom

    # Convert the total time to hours
    hours = total_time / 60
    result = hours
    return result

print(solution())