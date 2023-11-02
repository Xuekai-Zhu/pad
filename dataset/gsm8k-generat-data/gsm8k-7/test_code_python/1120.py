def solution():
    num_single_spreads = 20
    num_double_spreads = num_single_spreads * 2
    num_spread_pages = num_single_spreads + (num_double_spreads * 2)
    num_ads_per_block = 4
    num_quarter_pages_per_ad = 0.25
    num_blocks_per_spread = 1

    # Calculate the total number of pages printed for the ads
    num_ad_pages = (num_spread_pages / 4) * num_blocks_per_spread * num_ads_per_block * num_quarter_pages_per_ad

    # Calculate the total number of pages in the brochures
    total_brochure_pages = num_spread_pages + num_ad_pages

    # Calculate the total number of brochures that can be made
    num_brochures = total_brochure_pages // 5
    result = num_brochures
    return result

print(solution())