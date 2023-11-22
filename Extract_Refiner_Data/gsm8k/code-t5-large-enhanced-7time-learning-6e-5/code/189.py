def solution():
    
    # Define the initial number of pink plastic flamingos
    initial_flamingos = 18

    # Calculate the number of pink plastic flamingos after Friday
    friday_flamingos = initial_flamingos - 18

    # Calculate the number of pink plastic flamingos after Saturday
    saturday_flamingos = friday_flamingos / 3

    # Calculate the number of pink plastic flamingos after Sunday
    sunday_flamingos = saturday_flamingos + 18

    # Display the number of pink plastic flamingos after Sunday
    result = sunday_flamingos
    return result

print(solution())