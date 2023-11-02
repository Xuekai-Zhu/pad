def solution():
    """Pat is hunting for sharks to take photos. For every photo he takes he earns $15. He sees a shark about every 10 minutes. His boat fuel costs $50 an hour. If he shark hunts for 5 hours, how much money can he expect to make in profit?"""
    # Define the variables
    photo_value = 15
    shark_frequency = 1 / (10/60) # in sharks per hour
    fuel_cost = 50
    hours_hunting = 5

    # Calculate the expected number of photos taken
    expected_photos = shark_frequency * hours_hunting

    # Calculate the expected income from the photos
    expected_income = expected_photos * photo_value

    # Calculate the expected fuel cost
    expected_fuel_cost = fuel_cost * hours_hunting

    # Calculate the expected profit
    expected_profit = expected_income - expected_fuel_cost

    result = expected_profit
    return result

print(solution())