def solution():
    
    pretzels = 64
    goldfish = 4 * pretzels
    suckers = 32
    total_items = pretzels + goldfish + suckers
    items_per_baggie = total_items / 16
    result = items_per_baggie
    return result

print(solution())