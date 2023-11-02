def solution():
    """A printing press is printing brochures. The press prints 20 single-page spreads, and twice as many double-page spreads. For each 4 pages printed for the spreads, the press prints a block of 4 ads, each of which take up a quarter of a page. The brochures can be arranged in any order as long as they are made up of 5 pages each. How many brochures is the printing press creating?"""
    single_spreads = 20
    double_spreads = 2 * single_spreads
    total_spreads = single_spreads + double_spreads
    total_pages = (single_spreads * 1) + (double_spreads * 2)
    total_blocks = total_pages / 4
    total_ads = total_blocks * 4
    total_pages_with_ads = total_ads + total_pages
    brochures = total_pages_with_ads / 5
    result = brochures
    return result

print(solution())