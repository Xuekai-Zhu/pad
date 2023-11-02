def solution():
    """A cougar is sleeping for 4 hours at night, and a zebra for 2 hours more. How much time do both animals sleep in one week?"""
    # Define the number of hours each animal sleeps per day
    cougar_hours = 4
    zebra_hours = 6

    # Calculate the total number of hours each animal sleeps per week
    cougar_total = cougar_hours * 7
    zebra_total = zebra_hours * 7

    # Calculate the total number of hours both animals sleep per week
    total_sleep = cougar_total + zebra_total

    # Display the total number of hours both animals sleep per week
    result = total_sleep
    return result

print(solution())