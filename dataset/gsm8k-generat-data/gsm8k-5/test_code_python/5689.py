def solution():
    bunnies_per_minute = 3  # One bunny comes out of its burrow 3 times per minute
    total_bunnies = 20  # There are 20 bunnies

    # Calculate the total number of bunny burrow exits per minute for all bunnies
    burrow_exits_per_minute = bunnies_per_minute * total_bunnies

    # Calculate the total number of bunny burrow exits in 10 hours
    burrow_exits_per_10_hours = burrow_exits_per_minute * 60 * 10

    result = burrow_exits_per_10_hours
    return result

print(solution())