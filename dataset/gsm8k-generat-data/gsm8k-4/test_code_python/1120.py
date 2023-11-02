def solution():
    """A printing press is printing brochures. The press prints 20 single-page spreads, and twice as many double-page spreads. For each 4 pages printed for the spreads, the press prints a block of 4 ads, each of which take up a quarter of a page. The brochures can be arranged in any order as long as they are made up of 5 pages each. How many brochures is the printing press creating?"""
    # Define the number of single-page and double-page spreads
    single_spreads = 20
    double_spreads = 2 * single_spreads

    # Calculate the total number of pages of spreads
    total_spread_pages = single_spreads + (2 * double_spreads)

    # Calculate the total number of pages of ads
    total_ad_pages = (total_spread_pages // 4) * 1

    # Calculate the total number of pages, including spreads and ads
    total_pages = total_spread_pages + total_ad_pages

    # Calculate the number of brochures that can be created
    brochures = total_pages // 5

    result = brochures
    return result

print(solution())