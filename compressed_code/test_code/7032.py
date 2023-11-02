def solution():
    
    jamie_persians = 4
    jamie_mainecoons = 2
    gordon_persians = jamie_persians / 2
    gordon_mainecoons = jamie_mainecoons + 1
    hawkeye_mainecoons = gordon_mainecoons - 1
    total_cats = jamie_persians + jamie_mainecoons + gordon_persians + gordon_mainecoons + hawkeye_mainecoons
    result = total_cats
    return result

print(solution())