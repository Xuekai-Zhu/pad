def solution():
    """Jeff was driving to the capital city to attend a conference. At first, he was driving at 80 miles/hour for about 6 hours, then the speed limit changed and he had to slow down to 60 miles/hour, and so he drove at this speed for 4 hours. Then he made a stop at a gas station. Once the car was full of gas, he drove at 40 miles/hour the rest of the trip for 2 hours. How many miles did he travel?"""
    # Calculate the distance covered during the first leg of the trip
    leg1_distance = 80 * 6

    # Calculate the distance covered during the second leg of the trip
    leg2_distance = 60 * 4

    # Calculate the distance covered during the third leg of the trip
    leg3_distance = 40 * 2

    # Calculate the total distance covered
    total_distance = leg1_distance + leg2_distance + leg3_distance

    # Return the result
    result = total_distance
    return result

print(solution())