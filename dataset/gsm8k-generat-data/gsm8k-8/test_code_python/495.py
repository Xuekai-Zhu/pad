def solution():
    # Define the number of pretzels, goldfish, and suckers
    pretzels = 64
    goldfish = pretzels * 4
    suckers = 32

    # Define the number of items per baggie
    items_per_baggie = (pretzels + goldfish + suckers) / 16

    result = items_per_baggie
    return result

print(solution())