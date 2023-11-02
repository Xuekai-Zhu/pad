def solution():
    """Pat is hunting for sharks to take photos. For every photo he takes he earns $15. He sees a shark about every 10 minutes. His boat fuel costs $50 an hour. If he shark hunts for 5 hours, how much money can he expect to make in profit?"""
    photos_per_hour = 6
    price_per_photo = 15
    fuel_cost = 50 * 5
    total_photos = photos_per_hour * 5
    revenue = total_photos * price_per_photo
    profit = revenue - fuel_cost
    result = profit
    return result

print(solution())