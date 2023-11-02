def solution():
    """A truck can carry a maximum of 13,500 kgs of supplies. Yesterday, the truck was loaded with 100 boxes that weigh 100 kgs each. Then, it was loaded with 10 crates which weigh 60 kgs each. Today, it was loaded again with 50 sacks which weigh 50 kilograms each.
    How many bags weighing 40 kilograms each can we still load in the truck?"""
    max_weight = 13500
    yesterday_weight = 100 * 100
    today_weight = 10 * 60 + 50 * 50
    current_weight = yesterday_weight + today_weight
    remaining_weight = max_weight - current_weight
    bags_weight = 40
    bags_count = remaining_weight // bags_weight
    result = bags_count
    return result

print(solution())