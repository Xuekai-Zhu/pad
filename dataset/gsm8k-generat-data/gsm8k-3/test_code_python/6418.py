def solution():
    """Macy has a goal of running a total of 24 miles per week. If she runs 3 miles per day, how many miles does Macy have left to run after 6 days so that she could meet her goal?"""
    # Define the total number of miles Macy wants to run in a week
    GOAL_MILES = 24

    # Define the number of days that have passed
    days = 6

    # Calculate the total number of miles Macy has run so far
    miles_run = 3 * days

    # Calculate the number of miles Macy has left to run to meet her goal
    miles_left = GOAL_MILES - miles_run

    # Display the number of miles Macy has left to run
    result = miles_left
    return result

print(solution())