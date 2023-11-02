def solution():
    single_page_spreads = 20
    double_page_spreads = 2*single_page_spreads
    pages_for_spreads = single_page_spreads + double_page_spreads
    ads = pages_for_spreads/4
    brochures = ads/5
    result = brochures
    return result

print(solution())