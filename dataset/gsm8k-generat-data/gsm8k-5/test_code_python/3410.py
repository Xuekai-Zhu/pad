def solution():
    # Calculate the total cost of the rental
    weekday_rate = 420  # Rental rate for weekdays
    weekend_rate = 540  # Rental rate for weekends
    total_weekday_cost = 2 * weekday_rate  # Thursday and Friday are weekdays, for a total of 2 weekday rentals
    total_weekend_cost = 2 * weekend_rate  # Saturday and Sunday are weekends, for a total of 2 weekend rentals
    total_cost = total_weekday_cost + total_weekend_cost  # Total cost for 4 days

    # Calculate how much each person needs to pay
    number_of_people = 6  # Suzie and 5 friends
    amount_per_person = total_cost / number_of_people
    result = amount_per_person
    return result

print(solution())