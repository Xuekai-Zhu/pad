def solution():
    thor_age = 1456  # Thor is 1456 years old
    cap_ratio = 1/7  # Captain America is 1/7th of Peter Parker's age
    peter_age = (thor_age/13)/cap_ratio  # Peter Parker's age is calculated using ratios
    ironman_age = peter_age + 32  # Ironman's age is 32 years more than Peter Parker's age
    result = ironman_age
    return result

print(solution())