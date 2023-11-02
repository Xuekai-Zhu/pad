def solution():
    max_weight = 13500
    current_weight = 100 * 100 + 10 * 60   # weight of boxes and crates
    remaining_weight = max_weight - current_weight
    num_bags = remaining_weight // 50   # number of 50 kg bags we can still load
    num_bags_40kg = (num_bags // 2) * 3   # for every 2 bags, we can fit in 3 bags at 40 kgs each
    result = num_bags_40kg
    return result

print(solution())