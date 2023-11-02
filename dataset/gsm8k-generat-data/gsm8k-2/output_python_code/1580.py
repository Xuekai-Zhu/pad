def solution():
    """Jamie owns 4 Persian cats and 2 Maine Coons. Gordon owns half as many Persians and one more Maine Coon than Jamie.
    Hawkeye owns one less Maine Coon than Gordon and no Persian cats. If they bring all of their cats together to play, how many cats are there in total?"""
    jamie_persians = 4
    jamie_maine_coons = 2
    gordon_persians = jamie_persians / 2
    gordon_maine_coons = jamie_maine_coons + 1
    hawkeye_maine_coons = gordon_maine_coons - 1
    total_cats = jamie_persians + jamie_maine_coons + gordon_persians + gordon_maine_coons + hawkeye_maine_coons
    result = total_cats
    return result

print(solution())