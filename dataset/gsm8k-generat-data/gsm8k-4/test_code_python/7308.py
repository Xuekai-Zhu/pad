def solution():
    """Grant has four times as many vacations as Kelvin has classes. If Kelvin has 90 classes, how many vacations and classes do Grant and Kelvin have altogether?"""
    # Define Kelvin's number of classes
    kelvin_classes = 90

    # Calculate Grant's number of vacations
    grant_vacations = kelvin_classes * 4

    # Calculate the total number of classes and vacations
    total_classes = kelvin_classes
    total_vacations = grant_vacations

    # Add Kelvin's classes and Grant's vacations together
    total_classes_vacations = total_classes + total_vacations

    # return the result
    result = total_classes_vacations
    return result

print(solution())