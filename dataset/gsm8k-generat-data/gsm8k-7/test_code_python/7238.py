def solution():
    pack_per_mile = 0.5  # pounds of supplies per mile
    resupply_rate = 0.25  # the resupply will be 25% as large as the first pack
    hiking_speed = 2.5  # miles per hour
    daily_hiking_time = 8  # hours per day
    num_days = 5  # the trip will last for 5 days

    # Calculate the total distance the man will hike
    total_distance = hiking_speed * daily_hiking_time * num_days

    # Calculate the total weight of supplies needed for the trip, including the resupply
    total_weight = total_distance * pack_per_mile / (1 - resupply_rate)

    # Calculate the weight of supplies the man needs to bring with his first pack
    first_pack_weight = total_weight / (1 + resupply_rate)
    result = first_pack_weight
    return result

print(solution())