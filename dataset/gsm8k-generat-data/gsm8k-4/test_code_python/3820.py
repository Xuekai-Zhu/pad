def solution():
    """Jack needs to put his shoes on, then help both his toddlers tie their shoes. If it takes Jack 4 minutes to put his shoes on, and three minutes longer to help each toddler with their shoes, how long does it take them to get ready?"""
    # Define the time it takes Jack to put his shoes on and to help each toddler
    jack_shoes = 4
    toddler_shoes = 7

    # Calculate the total time it takes for everyone to get ready
    total_time = jack_shoes + (2*toddler_shoes)

    result = total_time
    return result

print(solution())