def solution():
    """Jason is climbing a telephone pole next to a tree his friend Matt is climbing. Matt can climb 6 feet/minute and Jason can climb 12 feet per minute. After 7 minutes, how much higher will Jason be than Matt?"""
    # Define Matt's climbing speed and the time elapsed
    matt_speed = 6
    time_elapsed = 7

    # Calculate how far Matt has climbed
    matt_height = matt_speed * time_elapsed

    # Define Jason's climbing speed
    jason_speed = 12

    # Calculate how far Jason has climbed
    jason_height = jason_speed * time_elapsed

    # Calculate the difference in height between Jason and Matt
    height_difference = jason_height - matt_height

    # Return the result
    result = height_difference
    return result

print(solution())