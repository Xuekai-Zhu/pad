def solution():
    """Georgina owns a parrot and is teaching it to speak. So far, the parrot knows seventeen phrases. If she is teaching it two phrases a week and it already knew three phrases when she bought it, how many days has Georgina had it?"""
    # Define the number of phrases the parrot knew when Georgina bought it
    initial_phrases = 3

    # Define the number of phrases added per week
    phrases_per_week = 2

    # Define the current number of phrases known by the parrot
    current_phrases = 17

    # Calculate the number of weeks Georgina has had the parrot
    weeks = (current_phrases - initial_phrases) / phrases_per_week

    # Calculate the number of days Georgina has had the parrot
    days = weeks * 7

    # Display the number of days Georgina has had the parrot
    result = days
    return result

print(solution())