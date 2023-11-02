def solution():
    total_pages = 500  # Anahi bought a 500 pages book
    pages_written_week1 = 150  # Anahi wrote on 150 pages in the first week
    pages_remaining_week2 = total_pages - pages_written_week1  # Anahi had this many pages left to write on in the second week

    # Anahi wrote on 30% of the remaining pages in the second week
    pages_written_week2 = 0.3 * pages_remaining_week2

    # Anahi damaged 20% of the empty pages she was to write on
    empty_pages_remaining = (total_pages - pages_written_week1 - pages_written_week2) * 0.8
    result = empty_pages_remaining
    return result

print(solution())