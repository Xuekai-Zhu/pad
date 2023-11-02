def solution():
    single_spider_legs = 8  # A single spider has 8 legs
    group_spiders = (single_spider_legs / 2) + 10  # The group has 10 more spiders than half as many legs as a single spider has

    # Calculate the total number of spider legs in the group
    total_legs = group_spiders * single_spider_legs
    result = total_legs
    return result

print(solution())