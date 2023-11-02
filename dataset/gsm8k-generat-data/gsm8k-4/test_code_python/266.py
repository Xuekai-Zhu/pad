def solution():
    """Johns goes to the gym 3 times a week. He spends 1 hour each day lifting weight. Additionally, he also spends a third of his weightlifting time warming up and doing cardio each day. How many hours does he spend at the gym a week?"""
    # Define the number of times John goes to the gym
    gym_days = 3

    # Define the time John spends lifting weights each gym day
    weightlifting_time = 1

    # Calculate the time John spends warming up and doing cardio each gym day
    cardio_time = weightlifting_time / 3

    # Calculate the total time John spends at the gym each day
    total_time = weightlifting_time + cardio_time

    # Calculate the total time John spends at the gym each week
    total_time_week = total_time * gym_days

    # Return the result
    result = total_time_week
    return result

print(solution())