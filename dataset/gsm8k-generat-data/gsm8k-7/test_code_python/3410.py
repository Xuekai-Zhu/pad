def solution():
    num_people = 6  # Suzie and 5 friends
    num_weekdays = 2  # Thursday and Friday
    num_weekend_days = 2  # Saturday and Sunday
    weekday_rate = 420
    weekend_rate = 540

    # Calculate the total cost of the rental
    total_cost = (num_weekdays * weekday_rate) + (num_weekend_days * weekend_rate)

    # Calculate how much each person has to pay
    cost_per_person = total_cost / num_people
    result = cost_per_person
    return result

print(solution())