def solution():
    """John and James decided to have a dance-off.  John danced for 3 hours and then another 5 hours after taking a 1-hour break.  James danced the whole time John was dancing and resting, and then another 1/3 times more hours.  How long was their combined dancing time without including John's break time?"""
    # Calculate John's total dancing time
    john_dancing_time = 3 + 5

    # Calculate James' dancing time
    james_dancing_time = john_dancing_time * 4 / 3

    # Calculate the total combined dancing time
    total_dancing_time = john_dancing_time + james_dancing_time

    # Display the total combined dancing time
    result = total_dancing_time
    return result

print(solution())