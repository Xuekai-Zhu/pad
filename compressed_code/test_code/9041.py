def solution():
    
    tinas_pail = 4
    tommy_pail = tinas_pail + 2
    timmy_pail = tommy_pail * 2
    trips = 3
    total_water = (tinas_pail + tommy_pail + timmy_pail) * trips
    result = total_water
    return result

print(solution())