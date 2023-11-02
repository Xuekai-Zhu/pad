def solution():
    virus_structure_temperature = 105.8
    venus_temperature = 900
    if virus_structure_temperature < venus_temperature:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())