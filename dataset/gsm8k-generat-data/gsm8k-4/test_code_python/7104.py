def solution():
    """A truck can carry a maximum of 13,500 kgs of supplies. Yesterday, the truck was loaded with 100 boxes that weigh 100 kgs each. Then, it was loaded with 10 crates which weigh 60 kgs each. Today, it was loaded again with 50 sacks which weigh 50 kilograms each. How many bags weighing 40 kilograms each can we still load in the truck?"""
    # Define the maximum weight capacity of the truck
    MAX_CAPACITY = 13500

    # Calculate the weight of the supplies already loaded on the truck
    loaded_weight = 100 * 100 + 10 * 60 + 50 * 50

    # Calculate the remaining weight capacity of the truck
    remaining_capacity = MAX_CAPACITY - loaded_weight

    # Calculate the number of bags that can still be loaded on the truck
    bags_weight = 40
    bags_capacity = bags_weight * remaining_capacity // 40

    result = bags_capacity
    return result

print(solution())