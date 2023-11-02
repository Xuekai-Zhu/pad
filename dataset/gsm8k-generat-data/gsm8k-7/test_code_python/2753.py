def solution():
    num_spiders = 3
    num_ants = 50

    eyes_per_spider = 8
    eyes_per_ant = 2

    # Calculate the total number of eyes among all spiders
    total_spider_eyes = num_spiders * eyes_per_spider

    #Calculate the total number of eyes among all ants
    total_ant_eyes = num_ants * eyes_per_ant

    # Calculate the total number of eyes among all of Nina's pet insects
    total_eyes = total_spider_eyes + total_ant_eyes
    result = total_eyes
    return result

print(solution())