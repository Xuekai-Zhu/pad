def solution():
    
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