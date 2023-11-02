def solution():
    """John invited 20 people to a birthday party. Each guest will eat 2 hot dogs. He already has 4 hot dogs left over from a previous party. If a pack of hot dogs contains 6 hot dogs and costs $2, how much does he need to spend on hot dogs?"""
    guests = 20
    hot_dogs_per_guest = 2
    leftovers = 4
    hot_dogs_needed = (guests * hot_dogs_per_guest) - leftovers
    hot_dogs_per_pack = 6
    packs_needed = hot_dogs_needed / hot_dogs_per_pack
    cost_per_pack = 2
    total_cost = packs_needed * cost_per_pack
    result = total_cost
    return result

print(solution())