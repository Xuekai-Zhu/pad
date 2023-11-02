def solution():
    """Reagan's school has a fish tank with a total of 280 fish of two types, koi fish and goldfish. Over the next 3 weeks, the school added 2 koi fish and 5 goldfish per day. If the tank had 200 goldfish at the end of the three weeks, what's the total number of koi fish in the tank after the three weeks?"""
    # Define the initial number of koi fish and goldfish
    koi_fish = 0
    goldfish = 0

    # Calculate the number of koi fish and goldfish added each day
    koi_added = 2
    gold_added = 5

    # Calculate the total number of days for which fish were added
    days_added = 3 * 7

    # Update the number of koi fish and goldfish based on the number added each day for the total number of days
    for i in range(days_added):
        koi_fish += koi_added
        goldfish += gold_added

    # Calculate the total number of fish in the tank after 3 weeks
    total_fish = koi_fish + goldfish

    # Calculate the number of koi fish in the tank after 3 weeks
    koi_fish_total = total_fish - 200

    # Display the total number of koi fish in the tank after 3 weeks
    result = koi_fish_total
    return result

print(solution())