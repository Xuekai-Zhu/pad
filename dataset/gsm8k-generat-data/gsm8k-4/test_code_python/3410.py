def solution():
    """Suzie and 5 of her friends decide to rent an Airbnb at Lake Tahoe for 4 days from Thursday to Sunday. The rental rate for weekdays is $420 per day. The weekend rental rate is $540 per day. They all decide to split the rental evenly. How much does each person have to pay?"""
    # Define the rental rates for weekdays and weekends
    WEEKDAY_RATE = 420
    WEEKEND_RATE = 540

    # Calculate the total rental cost
    total_rental_cost = (WEEKDAY_RATE * 2 + WEEKEND_RATE * 2) * 6

    # Calculate the rental cost per person
    rental_per_person = total_rental_cost / 6

    # Return the result rounded to two decimal places
    result = round(rental_per_person, 2)
    return result

print(solution())