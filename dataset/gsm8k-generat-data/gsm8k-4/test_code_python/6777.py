def solution():
    """Martin went on an eight-hour business trip. During the first half of the trip, he traveled at a speed of 70 kilometers per hour and during the second half at a speed of 85 kilometers per hour. How many kilometers did he travel during the journey?"""
    # Define the total duration of the trip
    total_duration = 8

    # Define the speeds for the first and second halves of the trip
    speed1 = 70
    speed2 = 85

    # Calculate the duration of the first half of the trip
    duration1 = total_duration / 2

    # Calculate the duration of the second half of the trip
    duration2 = total_duration - duration1

    # Calculate the distance traveled in the first half of the trip
    distance1 = speed1 * duration1

    # Calculate the distance traveled in the second half of the trip
    distance2 = speed2 * duration2

    # Calculate the total distance traveled
    total_distance = distance1 + distance2

    # Return the result
    result = total_distance
    return result

print(solution())