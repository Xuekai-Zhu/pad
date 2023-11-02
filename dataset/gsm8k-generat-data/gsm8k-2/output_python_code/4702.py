def solution():
    """Suzanna's history textbook has 160 pages and her geography textbook has 70 more pages. Her math textbook has half of the sum of the first two books' pages, and her science textbook has twice the number of pages of her history textbook. If Suzanna stacks all her textbooks on her desk, how many pages would there be in total?"""
    history_pages = 160
    geography_pages = history_pages + 70
    math_pages = (history_pages + geography_pages) / 2
    science_pages = 2 * history_pages
    total_pages = history_pages + geography_pages + math_pages + science_pages
    result = total_pages
    return result

print(solution())