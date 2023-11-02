def solution():
    """Suzie and 5 of her friends decide to rent an Airbnb at Lake Tahoe for 4 days from Thursday to Sunday. The rental rate for weekdays is $420 per day. The weekend rental rate is $540 per day. They all decide to split the rental evenly. How much does each person have to pay?"""
    # Define the rental rates for weekdays and weekends
    WEEKDAY_RATE = 420
    WEEKEND_RATE = 540

    # Calculate the total rental cost for the 4 days
    total_rental_cost = (2 * WEEKDAY_RATE + 2 * WEEKEND_RATE) + (2 * WEEKDAY_RATE + 2 * WEEKEND_RATE)

    # Calculate the amount each person needs to pay
    amount_per_person = total_rental_cost / 6

    # Display the amount each person needs to pay
    result = amount_per_person
    return result

print(solution())