def solution():
    """Mr. Maxwell takes 1 hr to drive to work in the morning but 1 and half hours to drive back home in the evening. If the morning and evening traffic is similar and he drives at an average speed of 30mph in the morning, what is the average speed of his return journey?"""
    # Define the distance to work
    distance = None

    # Calculate the distance to work using the average speed in the morning
    distance = 30 * 1

    # Calculate the average speed of the return journey using the distance and time taken in the evening
    average_speed = distance / (1.5)

    result = average_speed
    return result

print(solution())