def solution():
    """Jason is climbing a telephone pole next to a tree his friend Matt is climbing. Matt can climb 6 feet/minute and Jason can climb 12 feet per minute. After 7 minutes, how much higher will Jason be than Matt?"""
    # Define the climbing speeds of each person
    MATT_SPEED = 6 # feet per minute
    JASON_SPEED = 12 # feet per minute

    # Calculate the distance each person climbs in 7 minutes
    matt_distance = MATT_SPEED * 7 # feet
    jason_distance = JASON_SPEED * 7 # feet

    # Calculate the difference in height between Jason and Matt after 7 minutes
    height_difference = jason_distance - matt_distance # feet

    # Display the height difference
    result = height_difference
    return result

print(solution())