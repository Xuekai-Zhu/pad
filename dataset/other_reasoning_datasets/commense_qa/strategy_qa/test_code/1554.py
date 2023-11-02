def solution():
    birthrate = 0 # No information provided about birthrate
    deathrate = 0.007 # Bulgaria's population decreased by 0.7%
    if birthrate > deathrate:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())