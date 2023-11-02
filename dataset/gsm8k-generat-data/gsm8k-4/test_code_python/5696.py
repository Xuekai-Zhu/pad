def solution():
    """Georgina owns a parrot and is teaching it to speak. So far, the parrot knows seventeen phrases. If she is teaching it two phrases a week and it already knew three phrases when she bought it, how many days has Georgina had it?"""
    # Define the starting number of phrases the parrot knew
    starting_phrases = 3

    # Define the number of phrases the parrot learns per week
    phrases_per_week = 2

    # Define the current number of phrases known by the parrot
    current_phrases = 17

    # Calculate the number of weeks it has taken to teach the parrot these phrases
    weeks = (current_phrases - starting_phrases) / phrases_per_week

    # Calculate the number of days Georgina has had the parrot
    days = weeks * 7

    result = days
    return result

print(solution())