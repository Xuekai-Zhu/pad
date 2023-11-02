def solution():
    """Ivory and Brayan are doing school projects with a tight deadline and have to stay up late to complete everything. They prepare coffee to help them stay focused. If Brayan drinks twice as much coffee as Ivory, and Brayan drinks 4 cups of coffee in an hour, calculate the total number of cups of coffee they drink together in 5 hours."""
    brayan_coffee_per_hour = 4
    ivory_coffee_per_hour = brayan_coffee_per_hour / 2
    total_coffee_per_hour = brayan_coffee_per_hour + ivory_coffee_per_hour
    hours_coffee_was_consumed = 5
    total_coffee_consumed = total_coffee_per_hour * hours_coffee_was_consumed
    result = total_coffee_consumed
    return result

print(solution())