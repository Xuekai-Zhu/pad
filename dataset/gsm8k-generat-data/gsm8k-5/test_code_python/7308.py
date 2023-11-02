def solution():
    kelvin_classes = 90  # Kelvin has 90 classes
    grant_vacations = 4 * kelvin_classes  # Grant has four times as many vacations as Kelvin has classes
    
    # Calculate the total number of classes and vacations
    total_classes = kelvin_classes
    total_vacations = grant_vacations
    
    # Add the classes and vacations together for both Kelvin and Grant
    total_classes += kelvin_classes
    total_vacations += grant_vacations
    
    # Return the total number of classes and vacations
    result = (total_classes, total_vacations)
    return result

print(solution())