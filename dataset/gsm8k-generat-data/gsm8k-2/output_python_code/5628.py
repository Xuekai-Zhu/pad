def solution():
    """1/3 of the townspeople have received the full COVID vaccine. 1/3 are immune because they already recovered from COVID. If 1/6 of the townspeople are both vaccinated and already had COVID, what percent of the town is immune in some way?"""
    vaccine_percent = 1/3
    recovery_percent = 1/3
    vaccinated_and_recovered_percent = 1/6
    immune_percent = vaccine_percent + recovery_percent - vaccinated_and_recovered_percent
    result = immune_percent * 100
    return result

print(solution())