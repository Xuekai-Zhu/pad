def solution():
    """Zoey and Sydney are having a watermelon seed spitting contest. Whoever spits their seeds the most total distance wins. They each get one watermelon. Zoey's has 40 seeds and she spits each one 10 feet. Sydney's has 35 she spits each one 12 feet. What is the average total distance spat?"""
    zoey_seeds = 40
    zoey_distance_per_seed = 10
    zoey_total_distance = zoey_seeds * zoey_distance_per_seed

    sydney_seeds = 35
    sydney_distance_per_seed = 12
    sydney_total_distance = sydney_seeds * sydney_distance_per_seed

    total_distance = zoey_total_distance + sydney_total_distance
    average_distance = total_distance / 2
    result = average_distance
    return result

print(solution())