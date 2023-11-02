def solution():
    
    tina_pail = 4
    tommy_pail = tina_pail + 2
    timmy_pail = tommy_pail * 2
    total_water = 0
    for i in range(3):
        total_water += (tina_pail + tommy_pail + timmy_pail)
    result = total_water
    return result

print(solution())