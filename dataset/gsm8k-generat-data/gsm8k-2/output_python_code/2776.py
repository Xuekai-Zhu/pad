def solution():
    """Ivory and Brayan are doing school projects with a tight deadline and have to stay up late to complete everything. They prepare coffee to help them stay focused. If Brayan drinks twice as much coffee as Ivory, and Brayan drinks 4 cups of coffee in an hour, calculate the total number of cups of coffee they drink together in 5 hours."""
    brayan_cups_per_hour = 4
    ivory_cups_per_hour = brayan_cups_per_hour / 2
    total_cups = (brayan_cups_per_hour + ivory_cups_per_hour) * 5
    result = total_cups
    return result

print(solution())