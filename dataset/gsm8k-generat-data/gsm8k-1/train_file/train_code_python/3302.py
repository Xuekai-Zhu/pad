def solution():
    """Anahi bought a 500 pages book to write some notes on. In the first week, she wrote on 150 pages. In the second week, she wrote on 30% of the remaining pages. While continuing writing, she accidentally spilled coffee on the book and damaged 20 percent of the empty pages she was to write on. Calculate the total number of empty pages available for her to write on now."""
    total_pages = 500
    pages_written_1st_week = 150
    remaining_pages = total_pages - pages_written_1st_week
    pages_written_2nd_week = 0.3 * remaining_pages
    remaining_pages -= pages_written_2nd_week
    damaged_pages = 0.2 * remaining_pages
    empty_pages = remaining_pages - damaged_pages
    result = empty_pages
    return result

print(solution())