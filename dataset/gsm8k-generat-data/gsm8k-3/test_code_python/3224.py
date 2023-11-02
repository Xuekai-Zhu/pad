def solution():
    """Stephen rides his bicycle to church.  During the first third of his trip, he travels at a speed of 16 miles per hour. During the second third of his trip, riding uphill, he travels a speed of 12 miles per hour.  During the last third of his trip, he rides downhill at a speed of 20 miles per hour.  If each third of his trip takes 15 minutes, what is the distance Stephen rides his bicycle to church, in miles?"""
    # Define the speeds for each third of the trip
    speed1 = 16
    speed2 = 12
    speed3 = 20

    # Define the time for each third of the trip
    time = 0.25 # 15 minutes is 0.25 hours

    # Calculate the distances for each third of the trip
    distance1 = speed1 * time
    distance2 = speed2 * time
    distance3 = speed3 * time

    # Calculate the total distance of the trip
    total_distance = distance1 + distance2 + distance3

    # Display the total distance
    result = total_distance
    return result

print(solution())