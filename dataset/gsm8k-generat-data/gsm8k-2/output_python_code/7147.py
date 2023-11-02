def solution():
    """Reagan's school has a fish tank with a total of 280 fish of two types, koi fish and goldfish. Over the next 3 weeks, the school added 2 koi fish and 5 goldfish per day. If the tank had 200 goldfish at the end of the three weeks, what's the total number of koi fish in the tank after the three weeks?"""
    total_fish = 280
    initial_goldfish = total_fish - initial_koi_fish
    goldfish_added = 5 * 7 * 3  # 5 goldfish per day for 3 weeks
    total_goldfish = initial_goldfish + goldfish_added
    koi_fish_added = 2 * 7 * 3  # 2 koi fish per day for 3 weeks
    total_koi_fish = total_fish - total_goldfish
    final_koi_fish = total_koi_fish + koi_fish_added
    result = final_koi_fish
    return result

print(solution())