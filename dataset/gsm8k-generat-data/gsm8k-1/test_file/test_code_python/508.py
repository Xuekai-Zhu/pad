def solution():
    """Hannah needs to drink 60 ml of water for each kilometer she runs. If her gym teacher tells her to run 8 laps and each lap is 0.25 km, how many milliliters of water will Hannah need to drink?"""
    ml_per_km = 60
    laps = 8
    km_per_lap = 0.25
    total_km = laps * km_per_lap
    total_ml = total_km * ml_per_km
    result = total_ml
    return result

print(solution())