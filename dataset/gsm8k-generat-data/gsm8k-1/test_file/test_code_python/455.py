def solution():
    """A farmer is buying feed for his horses. He buys a variety of hay, oats, carrots and sugar cubes. Since sugar cubes are a rare treat, he only buys two 1-pound boxes of them for the whole stable. He only wants enough carrots to feed the horses while the vegetables are fresh, so he buys four 12-pound bags. Hay is the main diet of his horses, so he buys forty-two 75-pound bales. Oats are a staple to supplement the hay, so he buys twenty 65-pound sacks. If his farm truck can carry 2250 pounds at a time, how many trips does the farmer need to transport all the feed?"""
    sugar_cubes = 2
    carrot_bags = 4
    hay_bales = 42
    oats_sacks = 20
    sugar_weight = sugar_cubes * 1
    carrot_weight = carrot_bags * 12
    hay_weight = hay_bales * 75
    oats_weight = oats_sacks * 65
    total_weight = sugar_weight + carrot_weight + hay_weight + oats_weight
    trips_needed = total_weight // 2250 + 1
    result = trips_needed
    return result

print(solution())