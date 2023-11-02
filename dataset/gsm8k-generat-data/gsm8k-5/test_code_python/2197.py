def solution():
    obedient_yells = 12  # Missy yells at the obedient dog 12 times
    stubborn_yells = 4 * obedient_yells  # Missy yells at the stubborn dog 4 times for every 1 time she yells at the obedient dog
    total_yells = obedient_yells + stubborn_yells  # Missy yells at both dogs combined

    result = total_yells
    return result

print(solution())