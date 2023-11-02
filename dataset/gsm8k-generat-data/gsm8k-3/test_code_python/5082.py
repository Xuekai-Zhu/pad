def solution():
    """Lauren's social media channel makes $0.50 for every commercial that's viewed and $1.00 for every person who subscribes.  On Tuesday, 100 people watched commercials before viewing her content and 27 people subscribed.  How much money did she make?"""
    # Define the earnings per commercial viewed and per subscriber
    COMMERCIAL_EARNINGS = 0.5
    SUBSCRIBER_EARNINGS = 1.0

    # Get the number of commercials viewed and subscribers
    commercials_viewed = 100
    subscribers = 27

    # Calculate Lauren's earnings
    earnings = (commercials_viewed * COMMERCIAL_EARNINGS) + (subscribers * SUBSCRIBER_EARNINGS)

    # Display Lauren's earnings
    result = earnings
    return result

print(solution())