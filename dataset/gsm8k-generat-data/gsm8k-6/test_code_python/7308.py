def solution():
    # Calculate the number of vacations Grant has
    kelvin_classes = 90
    grant_vacations = 4 * kelvin_classes

    # Calculate the total number of vacations and classes Kelvin and Grant have
    total_classes = kelvin_classes
    total_vacations = kelvin_classes + grant_vacations
    
    result = (total_vacations, total_classes)
    return result

print(solution())