def solution():
    # Calculate the total distance the man will hike
    total_distance = 2.5 * 8 * 5  # he can hike at a rate of 2.5 mph for 8 hours a day for 5 days
    # Calculate the total weight of supplies he needs to bring for the entire hike, including the resupply
    total_weight = total_distance * 0.5 * 2  # he needs to pack about 0.5 pounds of supplies for every mile he hikes, and he will do it twice (first pack and resupply)
    # Calculate the weight of supplies he needs to bring with his first pack
    first_pack_weight = total_weight * 0.75  # the resupply will be 25% as large as his first pack
    result = first_pack_weight
    return result

print(solution())