def solution():
    tina_pail = 4
    tommy_pail = tina_pail + 2
    timmy_pail = tommy_pail * 2
    trips_each = 3
    total_water = (tina_pail + tommy_pail + timmy_pail) * trips_each
    result = total_water
    return result

print(solution())