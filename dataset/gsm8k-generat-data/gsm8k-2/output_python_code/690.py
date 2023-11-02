def solution():
    """Chance boarded a plane departing from London to New York at 6:00 a.m. ET on Monday. He arrived in New York 18 hours later. If he took another plane flying to Cape town the day he arrived in New York and arrived in Cape town at 10:00 a.m ET on Tuesday, calculate the number of hours his flight took from New York to cape town."""
    london_to_nyc_time = 18
    nyc_to_cape_town_time = 28
    total_time = nyc_to_cape_town_time - london_to_nyc_time
    result = total_time
    return result

print(solution())