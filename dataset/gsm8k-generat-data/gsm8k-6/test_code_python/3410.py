def solution():
    # Calculate the total rental cost for the 4 days
    weekdays_rental = 420 * 2
    weekend_rental = 540 * 2
    total_rental_cost = weekdays_rental + weekend_rental

    # Calculate the split rental cost per person
    split_rental_cost = total_rental_cost / 6  # 6 people split the rental evenly

    result = split_rental_cost
    return result

print(solution())