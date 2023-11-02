def solution():
    """In a week, Rayman works out for half the number of hours Junior takes to work out. Wolverine, their friend, works out for twice the combined total number of hours both Rayman and Junior take during their workouts. Calculate the number of hours Wolverine takes doing her workouts if Rayman does workouts for 10 hours in a week."""
    # Define the number of hours Rayman works out per week
    rayman_hours = 10

    # Calculate the number of hours Junior works out per week (double that of Rayman)
    junior_hours = rayman_hours * 2

    # Calculate the combined total number of hours both Rayman and Junior work out
    combined_hours = rayman_hours + junior_hours

    # Calculate the number of hours Wolverine works out (twice the combined total)
    wolverine_hours = combined_hours * 2

    # Return the result
    result = wolverine_hours
    return result

print(solution())