def solution():
    chinese_successor = "Chevrolet Monza"
    location_of_Monza = "near the north of Milan"
    if "Milan" not in chinese_successor and "Monza" in chinese_successor:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())