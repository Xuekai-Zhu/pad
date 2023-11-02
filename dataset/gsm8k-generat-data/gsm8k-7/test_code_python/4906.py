def solution():
    num_spiders = 8
    num_ants = 12

    # Calculate the total number of legs of all spiders
    total_spider_legs = num_spiders * 8

    # Calculate the total number of legs of all ants
    total_ant_legs = num_ants * 6

    # Calculate the total number of legs of the entire collection
    total_legs = total_spider_legs + total_ant_legs
    result = total_legs
    return result

print(solution())