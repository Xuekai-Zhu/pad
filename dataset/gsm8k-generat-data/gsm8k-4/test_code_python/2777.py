def solution():
    """Ivory and Brayan are doing school projects with a tight deadline and have to stay up late to complete everything. They prepare coffee to help them stay focused. If Brayan drinks twice as much coffee as Ivory, and Brayan drinks 4 cups of coffee in an hour, calculate the total number of cups of coffee they drink together in 5 hours."""
    # Calculate the number of cups of coffee Brayan drinks per hour
    brayan_coffee_per_hour = 4

    # Calculate the number of cups of coffee Ivory drinks per hour
    ivory_coffee_per_hour = brayan_coffee_per_hour / 2

    # Calculate the total number of cups of coffee they drink together in 5 hours
    total_coffee = (brayan_coffee_per_hour + ivory_coffee_per_hour) * 5

    # return the result
    result = total_coffee
    return result

print(solution())