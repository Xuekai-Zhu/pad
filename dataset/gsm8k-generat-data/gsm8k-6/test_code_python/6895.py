def solution():
    # Calculate the total dancing time of John
    john_dancing_time = 3 + 5 - 1  # John dances for 3 hours, then takes a 1 hour break, and then dances for 5 more hours

    # Calculate the total dancing time of James
    james_dancing_time = john_dancing_time + (1/3) * john_dancing_time  # James dances the whole time John is dancing and resting, and then for 1/3 more time

    # Calculate the combined dancing time of John and James (without John's break time)
    combined_dancing_time = john_dancing_time + james_dancing_time 

    result = combined_dancing_time
    return result

print(solution())