def solution():
    single_spider_legs = 8
    group_spiders = (single_spider_legs//2) + 10
    total_legs = group_spiders * single_spider_legs
    result = total_legs
    return result

print(solution())