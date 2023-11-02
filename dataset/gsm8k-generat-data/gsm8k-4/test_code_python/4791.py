def solution():
    """A cougar is sleeping for 4 hours at night, and a zebra for 2 hours more. How much time do both animals sleep in one week?"""
    # Define the sleeping time of each animal per night
    cougar_sleep = 4
    zebra_sleep = 6

    # Calculate the total sleeping time of both animals per night
    total_sleep = cougar_sleep + zebra_sleep

    # Calculate the total sleeping time of both animals in a week
    week_sleep = total_sleep * 7

    result = week_sleep
    return result

print(solution())