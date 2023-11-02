def solution():
    """Georgina owns a parrot and is teaching it to speak. So far, the parrot knows seventeen phrases. If she is teaching it two phrases a week and it already knew three phrases when she bought it, how many days has Georgina had it?"""
    known_phrases = 17
    phrases_taught_per_week = 2
    initial_known_phrases = 3
    days_owned = (known_phrases - initial_known_phrases) / phrases_taught_per_week * 7
    result = days_owned
    return result

print(solution())