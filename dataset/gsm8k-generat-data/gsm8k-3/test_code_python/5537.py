def solution():
    """Cody has an insurance plan that will give him a discount if he logs a total of 100,000 steps. For the first week, he logs 1,000 steps a day.  He increases his daily number of steps by 1,000 every week.  After 4 weeks how far away from his step goal will he be?"""
    # Define the number of steps Cody logs per day in the first week
    steps_per_day = 1000

    # Calculate the total number of steps Cody logs in the first week
    total_steps_week1 = steps_per_day * 7

    # Calculate the total number of steps Cody logs in the second week
    total_steps_week2 = (steps_per_day + 1000) * 7

    # Calculate the total number of steps Cody logs in the third week
    total_steps_week3 = (steps_per_day + 2000) * 7

    # Calculate the total number of steps Cody logs in the fourth week
    total_steps_week4 = (steps_per_day + 3000) * 7

    # Calculate the total number of steps over the 4 weeks
    total_steps = total_steps_week1 + total_steps_week2 + total_steps_week3 + total_steps_week4

    # Calculate the number of steps Cody needs to reach his goal
    steps_to_goal = 100000 - total_steps

    # Display the number of steps Cody needs to reach his goal
    result = steps_to_goal
    return result

print(solution())