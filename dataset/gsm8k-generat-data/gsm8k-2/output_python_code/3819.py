def solution():
    """Jack needs to put his shoes on, then help both his toddlers tie their shoes. If it takes Jack 4 minutes to put his shoes on, and three minutes longer to help each toddler with their shoes, how long does it take them to get ready?"""
    jack_shoes_time = 4
    toddler_shoes_time = 3
    total_time = jack_shoes_time + (2 * toddler_shoes_time)
    result = total_time
    return result

print(solution())