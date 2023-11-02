def solution():
    kelvin_classes = 90
    grant_vacations = kelvin_classes * 4
    total_classes = kelvin_classes
    total_vacations = grant_vacations + total_classes
    result = (total_classes, total_vacations)
    return result

print(solution())