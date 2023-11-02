def solution():
    total_spectators = 10000
    male_spectators = 7000
    female_spectators = total_spectators - male_spectators
    child_spectators = female_spectators / 5
    result = child_spectators
    return result

print(solution())