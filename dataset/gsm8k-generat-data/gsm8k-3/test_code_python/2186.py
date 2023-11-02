def solution():
    """Jeff was driving to the capital city to attend a conference. At first, he was driving at 80 miles/hour for about 6 hours, then the speed limit changed and he had to slow down to 60 miles/hour, and so he drove at this speed for 4 hours. Then he made a stop at a gas station. Once the car was full of gas, he drove at 40 miles/hour the rest of the trip for 2 hours. How many miles did he travel?"""
    
    # Calculate the distance traveled at 80 mph for 6 hours
    distance1 = 80 * 6

    # Calculate the distance traveled at 60 mph for 4 hours
    distance2 = 60 * 4

    # Calculate the distance traveled at 40 mph for 2 hours
    distance3 = 40 * 2

    # Calculate the total distance traveled
    total_distance = distance1 + distance2 + distance3

    # Display the total distance traveled
    result = total_distance
    return result

print(solution())