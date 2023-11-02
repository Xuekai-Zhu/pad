def solution():
    drops_per_feed = 20
    drops_per_liter = 5000
    liters_to_die = 3

    # Calculate the total number of drops of blood needed to die
    total_drops_to_die = liters_to_die * drops_per_liter

    # Calculate the number of mosquito feeds needed to reach that total
    num_feeds_to_die = total_drops_to_die / drops_per_feed
    result = num_feeds_to_die
    return result

print(solution())