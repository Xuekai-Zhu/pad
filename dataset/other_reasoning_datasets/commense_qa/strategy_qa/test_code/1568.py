def solution():
    genghis_khan_descendants = 16
    descendant_percentage = 0.005
    switzerland_population = 19000
    descendants_in_switzerland = switzerland_population * descendant_percentage
    if descendants_in_switzerland > 0:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())