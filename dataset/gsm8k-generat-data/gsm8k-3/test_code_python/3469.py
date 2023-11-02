def solution():
    """Calculate the number of hours Wolverine takes doing her workouts if Rayman does workouts for 10 hours in a week."""
    # Define Rayman's workout time
    rayman_workout = 10

    # Calculate Junior's workout time
    junior_workout = rayman_workout * 2

    # Calculate the combined workout time
    combined_workout = rayman_workout + junior_workout

    # Calculate Wolverine's workout time
    wolverine_workout = combined_workout * 2

    # Display Wolverine's workout time
    result = wolverine_workout
    return result

print(solution())