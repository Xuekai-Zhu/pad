def solution():
    total_distance = 200  # The total distance between the two towns is 200 miles
    distance_covered = total_distance * (1/4)  # Roger and his friend covered 1/4 of the total distance
    time_taken_first_leg = 1  # It took 1 hour to cover the first leg
    time_taken_lunch = 1  # They took a 1-hour lunch break
    speed = distance_covered / time_taken_first_leg  # Calculate the speed they traveled in the first leg
    distance_remaining = total_distance - distance_covered  # Calculate the remaining distance to be covered
    time_taken_second_leg = distance_remaining / speed  # Calculate the time taken to cover the remaining distance, at the same speed
    total_time = time_taken_first_leg + time_taken_lunch + time_taken_second_leg  # Calculate the total time taken
    result = total_time
    return result

print(solution())