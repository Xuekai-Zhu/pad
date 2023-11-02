def solution():
    """A printing press is printing brochures. The press prints 20 single-page spreads, and twice as many double-page spreads. For each 4 pages printed for the spreads, the press prints a block of 4 ads, each of which take up a quarter of a page. The brochures can be arranged in any order as long as they are made up of 5 pages each. How many brochures is the printing press creating?"""
    single_pages = 20
    double_pages = 2 * single_pages
    total_pages = single_pages + double_pages * 2
    num_blocks = total_pages // 4
    num_ads = num_blocks * 4
    total_pages += num_ads * 0.25
    num_brochures = total_pages // 5
    result = num_brochures
    return result

print(solution())