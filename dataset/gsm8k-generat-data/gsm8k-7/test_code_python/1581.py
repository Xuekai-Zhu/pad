def solution():
    jamie_persians = 4
    jamie_maine_coons = 2

    gordon_persians = jamie_persians / 2
    gordon_maine_coons = jamie_maine_coons + 1

    hawkeye_persians = 0
    hawkeye_maine_coons = gordon_maine_coons - 1

    total_cats = jamie_persians + jamie_maine_coons + gordon_persians + gordon_maine_coons + hawkeye_persians + hawkeye_maine_coons
    result = total_cats
    return result

print(solution())