def solution():
    # Calculate the total number of pages printed
    single_spreads = 20
    double_spreads = 2 * single_spreads
    total_spread_pages = single_spreads + 2 * double_spreads
    blocks_of_ads = total_spread_pages // 4
    total_ad_pages = blocks_of_ads * 4 * (1/4)
    total_printed_pages = total_spread_pages + total_ad_pages

    # Calculate the number of brochures that can be made
    num_brochures = total_printed_pages // 5
    
    result = num_brochures
    return result

print(solution())