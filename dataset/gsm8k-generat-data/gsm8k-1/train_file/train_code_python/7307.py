def solution():
    """Grant has four times as many vacations as Kelvin has classes. If Kelvin has 90 classes, how many vacations and classes do Grant and Kelvin have altogether?"""
    kelvin_classes = 90
    grant_vacations = kelvin_classes * 4
    total_classes = kelvin_classes + grant_vacations
    total_vacations = grant_vacations
    result = total_classes + total_vacations
    return result

print(solution())