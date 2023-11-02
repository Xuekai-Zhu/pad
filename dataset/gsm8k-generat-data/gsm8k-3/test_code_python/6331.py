def solution():
    """Anna can read 1 page in 1 minute. Carole can read as fast as Anna but at half the speed of Brianna. How long does it take Brianna to read a 100-page book?"""
    # Define Anna's reading speed
    ANNA_SPEED = 1 # page per minute

    # Define Carole's reading speed as half of Brianna's reading speed
    CAROLE_SPEED = 0.5 * 2 * ANNA_SPEED # page per minute

    # Calculate Brianna's reading speed
    BRIANNA_SPEED = 2 * ANNA_SPEED # page per minute

    # Calculate the time it takes Brianna to read a 100-page book
    time = 100 / BRIANNA_SPEED # minutes

    # Display the time in hours and minutes
    hours = int(time // 60)
    minutes = int(time % 60)

    result = f"{hours} hours and {minutes} minutes"
    return result

print(solution())