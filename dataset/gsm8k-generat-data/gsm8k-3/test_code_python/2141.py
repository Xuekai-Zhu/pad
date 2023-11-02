def solution():
    """Jerry mows 8 acres of lawn each week. He mows ¾ of it with a riding mower that can cut 2 acres an hour.
    He mows the rest with a push mower that can cut 1 acre an hour. How long does Jerry mow each week?"""
    # Define the amount of lawn mowed with the riding mower and push mower
    riding_mower_lawn = 8 * 0.75
    push_mower_lawn = 8 * 0.25

    # Calculate the time it takes to mow the lawn with the riding mower
    riding_mower_time = riding_mower_lawn / 2

    # Calculate the time it takes to mow the lawn with the push mower
    push_mower_time = push_mower_lawn

    # Calculate the total time it takes to mow the lawn
    total_time = riding_mower_time + push_mower_time

    # Display the total time
    result = total_time
    return result

print(solution())