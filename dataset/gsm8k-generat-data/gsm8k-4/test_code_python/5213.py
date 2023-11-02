def solution():
    """Jon decides to take up baseball. He can throw a fastball at 80 miles per hour. He goes through intense training 4 times for 4 weeks each time and at the end of the last one he can throw a ball 20% faster. How much speed (in mph) did he gain per week, assuming he gained an equal amount of speed (in mph) each week?"""
    # Define the initial fastball speed and the percentage increase
    initial_speed = 80
    percentage_increase = 0.2

    # Calculate the new fastball speed after the training
    new_speed = initial_speed * (1 + percentage_increase)

    # Calculate the number of weeks of training
    training_weeks = 4 * 4

    # Calculate the average increase in speed per week
    speed_increase_per_week = (new_speed - initial_speed) / training_weeks

    # Return the result
    result = speed_increase_per_week
    return result

print(solution())