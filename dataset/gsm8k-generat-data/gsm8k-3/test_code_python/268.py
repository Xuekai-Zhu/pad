def solution():
    """Johns goes to the gym 3 times a week.  He spends 1 hour each day lifting weight. Additionally, he also spends a third of his weightlifting time warming up and doing cardio each day.  How many hours does he spend at the gym a week?"""
    # Define the number of times John goes to the gym and the time spent lifting weights per day
    GYM_VISITS = 3
    WEIGHT_LIFTING_TIME = 1

    # Calculate the total time John spends at the gym per visit
    total_time = WEIGHT_LIFTING_TIME + (WEIGHT_LIFTING_TIME / 3)

    # Calculate the total time John spends at the gym per week
    weekly_time = total_time * GYM_VISITS

    # Display the total time John spends at the gym per week
    result = weekly_time
    return result

print(solution())