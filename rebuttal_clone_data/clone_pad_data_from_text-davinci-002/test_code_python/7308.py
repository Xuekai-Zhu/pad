def solution():
    kelvin_classes = 90
    grant_vacations = 4 * kelvin_classes
    total_vacations = grant_vacations + kelvin_classes
    total_classes = kelvin_classes + grant_vacations
    result = (total_vacations, total_classes)
    return result

print(solution())