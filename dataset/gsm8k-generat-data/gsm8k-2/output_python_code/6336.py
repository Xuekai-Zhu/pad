def solution():
    """There are 141 gold balloons and twice as many silver balloons. If the gold and silver balloons were added to 150 black balloons, how many balloons are there in total?"""
    gold_balloons = 141
    silver_balloons = 2 * gold_balloons
    black_balloons = 150
    total_balloons = gold_balloons + silver_balloons + black_balloons
    result = total_balloons
    return result

print(solution())