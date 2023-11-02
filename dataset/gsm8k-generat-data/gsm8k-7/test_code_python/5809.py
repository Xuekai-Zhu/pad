def solution():
    max_weight = 20  # kg
    num_crates = 15

    num_nail_bags = 4
    nail_bag_weight = 5  # kg per bag

    num_hammer_bags = 12
    hammer_bag_weight = 5  # kg per bag

    num_plank_bags = 10
    plank_weight = 30  # kg per bag

    # Calculate the total weight of all the nail bags
    total_nail_weight = num_nail_bags * nail_bag_weight

    # Calculate the total weight of all the hammer bags
    total_hammer_weight = num_hammer_bags * hammer_bag_weight

    # Calculate the total weight of all the plank bags
    total_plank_weight = num_plank_bags * plank_weight

    # Calculate the total weight of all the items
    total_weight = total_nail_weight + total_hammer_weight + total_plank_weight

    # Calculate the amount of weight that needs to be left out of the crates
    excess_weight = total_weight - (max_weight * num_crates)
    result = excess_weight
    return result

print(solution())