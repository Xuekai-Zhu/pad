def solution():
    """Georgina owns a parrot and is teaching it to speak. So far, the parrot knows seventeen phrases. If she is teaching it two phrases a week and it already knew three phrases when she bought it, how many days has Georgina had it?"""
    phrases_known = 17
    phrases_taught_per_week = 2
    initial_known_phrases = 3
    weeks_of_teaching = (phrases_known - initial_known_phrases) / phrases_taught_per_week
    days_of_teaching = weeks_of_teaching * 7
    result = days_of_teaching
    return result

print(solution())