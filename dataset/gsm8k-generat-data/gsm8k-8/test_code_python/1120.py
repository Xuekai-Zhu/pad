def solution():
    # Calculate the total number of pages printed for single-page spreads
    single_page_spreads = 20
    single_page_pages = single_page_spreads * 2

    # Calculate the total number of pages printed for double-page spreads
    double_page_spreads = 2 * single_page_spreads
    double_page_pages = double_page_spreads * 4

    # Calculate the total number of pages for spreads
    total_spread_pages = single_page_pages + double_page_pages

    # Calculate the total number of ad blocks printed
    total_ad_blocks = total_spread_pages // 4

    # Calculate the total number of pages for ads
    total_ad_pages = total_ad_blocks * 4

    # Calculate the total number of pages for brochures
    total_brochure_pages = total_spread_pages + total_ad_pages

    # Calculate the number of brochures
    num_brochures = total_brochure_pages // 5
    result = num_brochures
    return result

print(solution())