def solution():
    """4 students participated in a 200m race. If the average completion time of the last three students was 35 seconds, and the average completion time of all four runners was 30 seconds, how long (in seconds) did it take the student who came first to finish the race?"""
    # Define the number of students and the distance of the race
    num_students = 4
    race_distance = 200

    # Define the average completion time of all four runners
    avg_time_all = 30

    # Define the average completion time of the last three runners
    avg_time_last_three = 35

    # Calculate the total time taken by all four runners
    total_time_all = avg_time_all * num_students

    # Calculate the total time taken by the last three runners
    total_time_last_three = avg_time_last_three * (num_students - 1)

    # Calculate the time taken by the first student
    time_first = total_time_all - total_time_last_three

    # Calculate the speed of the first student
    speed_first = race_distance / time_first

    # Calculate the time taken by the first student to finish the race
    time_finish = race_distance / speed_first

    # Return the result in seconds
    result = time_finish
    return result

print(solution())