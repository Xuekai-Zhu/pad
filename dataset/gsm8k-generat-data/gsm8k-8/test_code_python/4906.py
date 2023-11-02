def solution():
    # Define the number of legs for each spider and ant
    spider_legs = 8
    ant_legs = 6

    # Calculate the total number of legs for the spiders and ants separately
    total_spider_legs = spider_legs * 8
    total_ant_legs = ant_legs * 12

    # Calculate the total number of legs for the entire collection
    total_legs = total_spider_legs + total_ant_legs
    result = total_legs
    return result

print(solution())