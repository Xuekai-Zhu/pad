def solution():
    coca_plant_climate = "humid tropical"
    yakutsk_climate = "extremely cold subarctic"
    if coca_plant_climate not in yakutsk_climate:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())