def solution():
    """Jairus read 20 pages of the newspaper. Arniel read 2 more than twice the number of pages Jairus read. How many pages have they read altogether?"""
    jairus_pages = 20
    arniel_pages = 2 + 2*jairus_pages
    total_pages = jairus_pages + arniel_pages
    result = total_pages
    return result

print(solution())