def solution():
    """John and James decided to have a dance-off. John danced for 3 hours and then another 5 hours after taking a 1-hour break. James danced the whole time John was dancing and resting, and then another 1/3 times more hours. How long was their combined dancing time without including John's break time?"""
    john_first_part = 3
    john_second_part = 5
    john_total = john_first_part + john_second_part
    james_resting_time = john_total
    james_total = john_total + (john_total / 3)
    total_dancing_time = john_total + james_total - james_resting_time
    result = total_dancing_time
    return result

print(solution())