def solution():
    """Reagan's school has a fish tank with a total of 280 fish of two types, koi fish and goldfish. Over the next 3 weeks, the school added 2 koi fish and 5 goldfish per day. If the tank had 200 goldfish at the end of the three weeks, what's the total number of koi fish in the tank after the three weeks?"""
    total_fish = 280
    added_koi_per_day = 2
    added_goldfish_per_day = 5
    weeks = 3

    for i in range(weeks):
        total_fish += added_koi_per_day + added_goldfish_per_day

    goldfish_in_tank = 200
    koi_in_tank = total_fish - goldfish_in_tank
    result = koi_in_tank
    return result

print(solution())