def solution():
    Brayan_drinks = 4  # Brayan drinks 4 cups of coffee in an hour
    Ivory_drinks = Brayan_drinks / 2  # Ivory drinks half as much coffee as Brayan

    # Calculate the total number of cups of coffee they drink together in 5 hours
    total_drinks = (Brayan_drinks + Ivory_drinks) * 5

    result = total_drinks
    return result

print(solution())