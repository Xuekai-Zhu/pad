def solution():
    mL_per_tube = 7
    tube_count = 6
    beaker_count = 3
    total_mL = mL_per_tube * tube_count
    mL_per_beaker = total_mL / beaker_count
    result = mL_per_beaker
    return result

print(solution())