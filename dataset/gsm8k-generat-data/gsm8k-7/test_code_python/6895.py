def solution():
    john_dancing_time = 3 + 5  # John danced for 3 hours and then another 5 hours after taking a 1-hour break.
    james_dancing_time = john_dancing_time * (4/3)  # James danced the whole time John was dancing and resting, and then another 1/3 times more hours.

    # Calculate the combined dancing time of John and James without including John's break time
    combined_dancing_time = john_dancing_time + james_dancing_time

    result = combined_dancing_time
    return result

print(solution())