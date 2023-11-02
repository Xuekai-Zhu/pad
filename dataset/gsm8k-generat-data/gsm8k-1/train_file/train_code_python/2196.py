def solution():
    """Missy has an obedient dog and a stubborn dog. She has to yell at the stubborn dog four times for every one time she yells at the obedient dog. If she yells at the obedient dog 12 times, how many times does she yell at both dogs combined?"""
    obedient_yells = 12
    stubborn_yells = 4 * obedient_yells
    total_yells = obedient_yells + stubborn_yells
    result = total_yells
    return result

print(solution())