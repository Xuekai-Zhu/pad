def solution():
    nickel_boiling_point = 3003
    outer_core_temperature = 3500 # Assuming an average temperature
    if nickel_boiling_point > outer_core_temperature:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())