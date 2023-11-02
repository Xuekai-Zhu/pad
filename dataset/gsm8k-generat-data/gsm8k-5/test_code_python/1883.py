def solution():
    total_scuba_diving_time = 8  # Jim spends 8 hours scuba diving
    total_gold_found = 100 + (2 * (0.5 * 100))  # Jim finds 100 gold coins in a treasure chest and 2 smaller bags with half as much gold each
    gold_found_per_hour = total_gold_found / total_scuba_diving_time  # Calculate gold found per hour

    result = gold_found_per_hour
    return result

print(solution())