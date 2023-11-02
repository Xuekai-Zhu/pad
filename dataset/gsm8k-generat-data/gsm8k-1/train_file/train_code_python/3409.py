def solution():
    """Suzie and 5 of her friends decide to rent an Airbnb at Lake Tahoe for 4 days from Thursday to Sunday. 
    The rental rate for weekdays is $420 per day. The weekend rental rate is $540 per day. 
    They all decide to split the rental evenly. How much does each person have to pay?"""
    
    weekdays_rate = 420
    weekend_rate = 540
    days_weekdays = 2  # Thursday and Friday
    days_weekend = 2  # Saturday and Sunday
    total_rent = (weekdays_rate * days_weekdays) + (weekend_rate * days_weekend)
    num_people = 6  # Suzie and 5 friends
    rent_per_person = total_rent / num_people
    result = rent_per_person
    return result

print(solution())