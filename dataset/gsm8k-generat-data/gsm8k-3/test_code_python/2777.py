def solution():
    """Ivory and Brayan are doing school projects with a tight deadline and have to stay up late to complete everything. They prepare coffee to help them stay focused. If Brayan drinks twice as much coffee as Ivory, and Brayan drinks 4 cups of coffee in an hour, calculate the total number of cups of coffee they drink together in 5 hours."""
    # Define Brayan's coffee intake per hour
    BRAYAN_PER_HOUR = 4

    # Calculate Ivory's coffee intake per hour
    ivory_per_hour = BRAYAN_PER_HOUR / 2

    # Calculate the total amount of coffee they drink together in 5 hours
    total_coffee = (ivory_per_hour + BRAYAN_PER_HOUR) * 5

    # Display the total amount of coffee they drink
    result = total_coffee
    return result

print(solution())