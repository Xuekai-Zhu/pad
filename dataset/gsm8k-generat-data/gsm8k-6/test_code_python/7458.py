def solution():
    # Calculate the total distance covered by Polly in one half hour
    distance_Polly = 12 * 1/4  # Polly circles the track 12 times, and the track is a quarter mile circular track

    # Calculate the average speed of Polly
    speed_Polly = distance_Polly / (1/2)  # time taken by Polly to cover the distance is 30 minutes or 1/2 hour

    # Calculate the speed of Gerald's car
    speed_Gerald = speed_Polly / 2  # Gerald's car moves at half the speed of Polly's car

    # Convert the speed to miles per hour
    speed_Gerald_mph = speed_Gerald * 2.23694  # 1 meter per second is equal to 2.23694 miles per hour

    result = speed_Gerald_mph
    return result

print(solution())