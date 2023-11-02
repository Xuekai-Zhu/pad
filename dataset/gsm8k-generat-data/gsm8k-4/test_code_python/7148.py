def solution():
    """Reagan's school has a fish tank with a total of 280 fish of two types, koi fish and goldfish. Over the next 3 weeks, the school added 2 koi fish and 5 goldfish per day. If the tank had 200 goldfish at the end of the three weeks, what's the total number of koi fish in the tank after the three weeks?"""
    # Define the initial number of koi and goldfish in the tank
    initial_koi = None
    initial_goldfish = None

    # Define the number of days in 3 weeks
    days = 21

    # Define the number of koi and goldfish added per day
    koi_add = 2
    goldfish_add = 5

    # Calculate the final number of goldfish
    final_goldfish = 200

    # Calculate the total number of fish added in 3 weeks
    total_fish_added = (koi_add + goldfish_add) * days

    # Calculate the new number of koi fish in the tank
    final_koi = total_fish_added + initial_koi - (initial_koi / initial_goldfish) * (initial_goldfish - final_goldfish)

    result = int(final_koi)
    return result

print(solution())