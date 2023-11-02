def solution():
    geographer_area_of_study = "geography"
    biochemistry_area_of_study = "biochemistry"
    if biochemistry_area_of_study in geographer_area_of_study:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())