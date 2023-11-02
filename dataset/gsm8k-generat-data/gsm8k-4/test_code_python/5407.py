def solution():
    """Jill has a difficult test to study for. She decides to study one day for 2 hours. The next day she doubles this amount, and the day after that she studies one hour less than the previous day. How many minutes does Jill study over the 3 days?"""
    # Define the initial study time and the reduction in study time each day
    initial_study_time = 2  # in hours
    reduction = 1  # in hours

    # Calculate the study time for each day
    day1_time = initial_study_time * 60  # in minutes
    day2_time = (initial_study_time * 2) * 60  # in minutes
    day3_time = (initial_study_time * 2 - reduction) * 60  # in minutes

    # Calculate the total study time over three days
    total_study_time = day1_time + day2_time + day3_time

    # return the result
    return total_study_time

print(solution())