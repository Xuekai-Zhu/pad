def solution():
    john_dancing_time = 3 + 5  # John danced for 3 hours, took a 1-hour break, and then danced for 5 more hours
    james_dancing_time = john_dancing_time  # James danced the whole time John was dancing and resting

    # Calculate the additional time James danced
    additional_time = john_dancing_time * (1/3)
    james_dancing_time += additional_time

    # Calculate the total combined dancing time without including John's break time
    total_dancing_time = john_dancing_time + james_dancing_time
    result = total_dancing_time
    return result

print(solution())