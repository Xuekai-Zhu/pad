def solution():
    """Rhonda, Sally, and Diane are members of their school's track team. The three of them run the 600-meter relay race together. Rhonda runs the first 200 meters of the race, Sally runs the second 200 meters of the race, and Diane runs the final 200 meters of the race. Rhonda can run 200 meters in 24 seconds. Sally takes two seconds longer to run the same distance, while Diane can run 200 meters three seconds faster than Rhonda. How many seconds does it take for the three of them to run the 600-meter relay race?"""
    # Define Rhonda's time to run 200 meters
    rhonda_time = 24

    # Define Sally's time to run 200 meters
    sally_time = rhonda_time + 2

    # Define Diane's time to run 200 meters
    diane_time = rhonda_time - 3

    # Calculate the total time for the relay race
    total_time = rhonda_time + sally_time + diane_time

    # return the result
    result = total_time
    return result

print(solution())