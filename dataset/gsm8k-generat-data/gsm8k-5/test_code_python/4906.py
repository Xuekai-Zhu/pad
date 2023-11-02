def solution():
    legs_per_spider = 8  # Each spider has 8 legs
    legs_per_ant = 6  # Each ant has 6 legs
    total_spiders = 8  # Monroe has 8 spiders in his collection
    total_ants = 12  # Monroe has 12 ants in his collection

    # Calculate the total number of legs in the collection
    total_legs = (legs_per_spider * total_spiders) + (legs_per_ant * total_ants)
    result = total_legs
    return result

print(solution())