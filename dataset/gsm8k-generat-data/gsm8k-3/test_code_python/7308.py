def solution():
    """Grant has four times as many vacations as Kelvin has classes. If Kelvin has 90 classes, how many vacations and classes do Grant and Kelvin have altogether?"""
    # Define the ratio of Grant's vacations to Kelvin's classes
    GRANT_RATIO = 4

    # Define Kelvin's number of classes
    kelvin_classes = 90

    # Calculate Grant's number of vacations
    grant_vacations = kelvin_classes * GRANT_RATIO

    # Calculate the total number of classes and vacations for Kelvin and Grant
    total_classes = kelvin_classes
    total_vacations = grant_vacations

    # Display the total number of classes and vacations
    result = total_classes + total_vacations
    return result

print(solution())