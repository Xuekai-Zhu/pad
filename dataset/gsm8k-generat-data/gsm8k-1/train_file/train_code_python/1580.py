def solution():
    """Jamie owns 4 Persian cats and 2 Maine Coons. Gordon owns half as many Persians and one more Maine Coon than Jamie. Hawkeye owns one less Maine Coon than Gordon and no Persian cats. If they bring all of their cats together to play, how many cats are there in total?"""
    jamie_persians = 4
    jamie_mainecoons = 2
    gordon_persians = jamie_persians / 2
    gordon_mainecoons = jamie_mainecoons + 1
    hawkeye_mainecoons = gordon_mainecoons - 1
    total_cats = jamie_persians + jamie_mainecoons + gordon_persians + gordon_mainecoons + hawkeye_mainecoons
    result = total_cats
    return result

print(solution())