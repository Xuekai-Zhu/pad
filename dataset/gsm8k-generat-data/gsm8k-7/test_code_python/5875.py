def solution():
    lana_pages = 8  # initial number of blank pages in Lana's binder
    duane_pages = 42 // 2  # half of the pages in Duane's binder

    # Lana gains the pages Duane gives her
    lana_pages += duane_pages

    result = lana_pages
    return result

print(solution())