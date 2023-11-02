def solution():
    """Suzie and 5 of her friends decide to rent an Airbnb at Lake Tahoe for 4 days from Thursday to Sunday. The rental rate for weekdays is $420 per day. The weekend rental rate is $540 per day. They all decide to split the rental evenly. How much does each person have to pay?"""
    weekday_rate = 420
    weekend_rate = 540
    rental_days = 4
    total_weekday_rental = weekday_rate * 2  # Thursday and Friday
    total_weekend_rental = weekend_rate * 2  # Saturday and Sunday
    total_rental_cost = total_weekday_rental + total_weekend_rental
    cost_per_person = total_rental_cost / 6  # 6 people splitting the rental
    result = cost_per_person
    return result

print(solution())