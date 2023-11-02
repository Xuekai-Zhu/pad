def solution():
    """Kevin is taking a 600-mile trip, traveling at a rate of 50 miles per hour. How much faster must he travel to decrease his travel time by 4 hours?"""
    # Calculate Kevin's original travel time
    original_time = 600 / 50

    # Calculate Kevin's new travel time with a 4-hour decrease
    new_time = original_time - 4

    # Calculate the new speed needed to achieve the decrease in travel time
    new_speed = 600 / new_time - 50

    # Display the new speed needed
    result = new_speed
    return result

print(solution())