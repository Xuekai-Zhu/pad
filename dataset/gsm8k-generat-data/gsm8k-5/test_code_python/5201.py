def solution():
    total_distance = 2 * 3  # The total distance between the first and third station is 2 hours apart, times 3 segments
    speed = total_distance / 2.5  # Kira takes 2.5 hours to travel from the first to third station, including the break
    total_time = 2.5 * 60  # Convert the total time to minutes
    result = total_time
    return result

print(solution())