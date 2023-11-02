def solution():
    """Aren’s flight from New York to Hawaii will take 11 hours 20 minutes. He spends 2 hours reading, 4 hours watching two movies, 30 minutes eating his dinner, 40 minutes listening to the radio, and 1 hour 10 minutes playing games. How many hours does he have left to take a nap?"""
    flight_time = 11 + 20/60
    total_non_nap_time = 2 + 4 + 0.5 + 0.67 + 1.17
    nap_time = flight_time - total_non_nap_time
    result = nap_time
    return result

print(solution())