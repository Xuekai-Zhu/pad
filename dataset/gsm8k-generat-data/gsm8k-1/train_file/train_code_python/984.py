def solution():
    """James has an old printer that crumples every seventh page and blurs the ink on every third page. If he prints 42 pages, how many are neither crumpled or blurred?"""
    num_pages = 42
    crumpled_pages = num_pages // 7
    blurred_pages = num_pages // 3
    crumpled_and_blurred_pages = num_pages // 21
    good_pages = num_pages - (crumpled_pages + blurred_pages - crumpled_and_blurred_pages)
    result = good_pages
    return result

print(solution())