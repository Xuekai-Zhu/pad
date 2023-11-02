def solution():
    """A fog bank rolls in from the ocean to cover a city. It takes 10 minutes to cover every 3 miles of the city. If the city is 42 miles across from the oceanfront to the opposite inland edge, how many minutes will it take for the fog bank to cover the whole city?"""
    miles_per_interval = 3
    city_width = 42
    intervals_to_cover_city = city_width / miles_per_interval
    minutes_to_cover_interval = 10
    total_minutes_to_cover_city = intervals_to_cover_city * minutes_to_cover_interval
    result = total_minutes_to_cover_city
    return result

print(solution())