def solution():
    # Calculate total number of days rented
    total_days = 4

    # Calculate number of weekdays and weekends
    weekdays = 2
    weekends = 2

    # Calculate total cost of rental
    weekday_cost = 420 * weekdays
    weekend_cost = 540 * weekends
    total_cost = weekday_cost + weekend_cost

    # Calculate cost per person
    num_people = 6
    cost_per_person = total_cost / num_people

    result = cost_per_person
    return result

print(solution())