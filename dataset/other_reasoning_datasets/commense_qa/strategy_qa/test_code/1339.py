def solution():
    jay_z_birth_year = 1969
    louis_armstrong_death_year = 1971
    # Since Louis Armstrong died before Jay-Z was of collaborating age, the answer is "no"
    if jay_z_birth_year >= (louis_armstrong_death_year + 18):
        result = "yes"
    else:
        result = "no"
    return result

print(solution())