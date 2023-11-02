def solution():
    pretzels = 64
    goldfish = pretzels * 4
    suckers = 32
    total_snacks = pretzels + goldfish + suckers
    snacks_per_bag = total_snacks / 16
    result = snacks_per_bag
    return result

print(solution())