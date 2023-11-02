def solution():
    """Jack needs to put his shoes on, then help both his toddlers tie their shoes. If it takes Jack 4 minutes to put his shoes on, and three minutes longer to help each toddler with their shoes, how long does it take them to get ready?"""
    time_for_jack = 4
    time_per_toddler = 3
    num_toddlers = 2
    total_time = time_for_jack + (time_per_toddler * num_toddlers)
    result = total_time
    return result

print(solution())