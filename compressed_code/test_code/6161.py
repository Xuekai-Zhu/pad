def solution():
    
    pretzels = 64
    goldfish = pretzels * 4
    suckers = 32
    num_of_baggies = 16
    total_items = pretzels + goldfish + suckers
    items_per_baggie = total_items // num_of_baggies
    result = items_per_baggie
    return result

print(solution())