def solution():
    # Calculate Gordon's number of cats
    gordon_persians = 4 / 2
    gordon_maine_coons = 2 + 1
    gordon_total_cats = gordon_persians + gordon_maine_coons

    # Calculate Hawkeye's number of cats
    hawkeye_persians = 0
    hawkeye_maine_coons = gordon_maine_coons - 1
    hawkeye_total_cats = hawkeye_persians + hawkeye_maine_coons

    # Calculate the total number of cats
    total_cats = 4 + 2 + gordon_total_cats + hawkeye_total_cats
    result = total_cats
    return result

print(solution())