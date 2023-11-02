def solution():
    """Anahi bought a 500 pages book to write some notes on. In the first week, she wrote on 150 pages. In the second week, she wrote on 30% of the remaining pages. While continuing writing, she accidentally spilled coffee on the book and damaged 20 percent of the empty pages she was to write on. Calculate the total number of empty pages available for her to write on now."""
    total_pages = 500
    written_pages_1 = 150
    remaining_pages_1 = total_pages - written_pages_1
    written_pages_2 = 0.3 * remaining_pages_1
    remaining_pages_2 = remaining_pages_1 - written_pages_2
    damaged_pages = 0.2 * remaining_pages_2
    empty_pages = remaining_pages_2 - damaged_pages
    result = empty_pages
    return result

print(solution())