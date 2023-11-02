def solution():
    """Pat is hunting for sharks to take photos. For every photo he takes he earns $15. He sees a shark about every 10 minutes. His boat fuel costs $50 an hour. If he shark hunts for 5 hours, how much money can he expect to make in profit?"""
    photo_value = 15
    shark_frequency = 1 / 10 # sharks seen per minute
    total_minutes = 5 * 60 # minutes in 5 hours
    total_sharks = shark_frequency * total_minutes
    total_photos = total_sharks
    total_earnings = total_photos * photo_value
    fuel_cost = 50 * 5 # $50 per hour for 5 hours
    profit = total_earnings - fuel_cost
    result = profit
    return result

print(solution())