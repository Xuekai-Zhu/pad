def solution():
    """Jeff was driving to the capital city to attend a conference. At first, he was driving at 80 miles/hour for about 6 hours,
    then the speed limit changed and he had to slow down to 60 miles/hour, and so he drove at this speed for 4 hours.
    Then he made a stop at a gas station. Once the car was full of gas, he drove at 40 miles/hour the rest of the trip for 2 hours.
    How many miles did he travel?"""
    dist_first_leg = 80 * 6
    dist_second_leg = 60 * 4
    dist_third_leg = 40 * 2
    total_distance = dist_first_leg + dist_second_leg + dist_third_leg
    result = total_distance
    return result

print(solution())