def solution():
    """Jeff was driving to the capital city to attend a conference. At first, he was driving at 80 miles/hour for about 6 hours, then the speed limit changed and he had to slow down to 60 miles/hour, and so he drove at this speed for 4 hours. Then he made a stop at a gas station. Once the car was full of gas, he drove at 40 miles/hour the rest of the trip for 2 hours. How many miles did he travel?"""
    first_leg_speed = 80
    first_leg_time = 6
    first_leg_distance = first_leg_speed * first_leg_time

    second_leg_speed = 60
    second_leg_time = 4
    second_leg_distance = second_leg_speed * second_leg_time

    third_leg_speed = 40
    third_leg_time = 2
    third_leg_distance = third_leg_speed * third_leg_time

    total_distance = first_leg_distance + second_leg_distance + third_leg_distance
    result = total_distance
    return result

print(solution())