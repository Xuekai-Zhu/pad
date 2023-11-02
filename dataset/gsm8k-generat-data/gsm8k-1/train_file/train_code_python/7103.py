def solution():
    """A truck can carry a maximum of 13,500 kgs of supplies. Yesterday, the truck was loaded with 100 boxes that weigh 100 kgs each. Then, it was loaded with 10 crates which weigh 60 kgs each. Today, it was loaded again with 50 sacks which weigh 50 kilograms each. How many bags weighing 40 kilograms each can we still load in the truck?"""
    max_capacity = 13500
    current_load = 100*100 + 10*60 + 50*50
    remaining_capacity = max_capacity - current_load
    weight_per_bag = 40
    bags_to_load = remaining_capacity // weight_per_bag
    result = bags_to_load
    return result

print(solution())