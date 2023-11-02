def solution():
    """At the Mystic Aquarium, sharks are fed four buckets of fish each day. The dolphins are fed half as many buckets as the sharks while the other sea animals are fed five times as many buckets as the sharks. How many weeks will 546 buckets of fish last?"""
    # Define the number of buckets of fish needed per day for each type of animal
    sharks_daily = 4
    dolphins_daily = sharks_daily / 2
    other_animals_daily = sharks_daily * 5

    # Calculate the total number of buckets of fish needed per day
    total_daily = sharks_daily + dolphins_daily + other_animals_daily

    # Calculate the number of days that 546 buckets of fish will last
    days = 546 / total_daily

    # Calculate the number of weeks that 546 buckets of fish will last
    weeks = days / 7

    result = weeks
    return result

print(solution())