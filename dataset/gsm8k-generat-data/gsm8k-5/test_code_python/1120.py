def solution():
    single_page_spreads = 20
    double_page_spreads = 2 * single_page_spreads
    total_spreads = single_page_spreads + double_page_spreads
    pages_per_spread = 2  # 1 page for a single-page spread, 2 pages for a double-page spread
    total_pages = total_spreads * pages_per_spread

    # Calculate the number of blocks of 4 ads that will be printed
    ads_per_block = 4
    pages_per_block = 4
    blocks_of_ads = total_pages // pages_per_block

    # Subtract the ads from the total number of pages to get the number of brochure pages
    brochure_pages = total_pages - (blocks_of_ads * ads_per_block)

    # Calculate the number of brochures that can be created
    pages_per_brochure = 5
    num_brochures = brochure_pages // pages_per_brochure
    result = num_brochures
    return result

print(solution())