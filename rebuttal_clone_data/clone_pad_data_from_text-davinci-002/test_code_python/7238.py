def solution():
    miles_to_hike = (8 * 5) / 2.5  # this calculates the number of miles the man will hike
    initial_supplies = miles_to_hike * 0.5  # this calculates the amount of supplies he will need for the entire hike
    resupply = initial_supplies * 0.25  # this calculates the amount of supplies he will get from his one resupply
    total_supplies = initial_supplies + resupply  # this calculates the total amount of supplies he will need for the hike
    first_pack = initial_supplies  # this calculates the amount of supplies he will need to bring with his first pack
 
    result = first_pack
 
    return result

print(solution())