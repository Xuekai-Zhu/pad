def solution():
    """Jack needs to put his shoes on, then help both his toddlers tie their shoes. If it takes Jack 4 minutes to put his shoes on, and three minutes longer to help each toddler with their shoes, how long does it take them to get ready?"""
    # Define the time it takes Jack to put his shoes on and help each toddler
    JACK_SHOES_TIME = 4
    TODDLER_SHOES_TIME = 7 # 4 for Jack's shoes + 3 for each toddler's shoes

    # Calculate the total time it takes them to get ready
    total_time = JACK_SHOES_TIME + 2*TODDLER_SHOES_TIME # Jack helps 2 toddlers

    # Display the total time
    result = total_time
    return result

print(solution())