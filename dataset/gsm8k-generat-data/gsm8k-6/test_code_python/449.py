def solution():
    single_spider_legs = 8  # number of legs on a single spider
    group_of_spiders = (single_spider_legs / 2) + 10  # number of spiders in the group
    total_legs = group_of_spiders * single_spider_legs  # total number of spider legs in the group
    result = total_legs
    return result

print(solution())