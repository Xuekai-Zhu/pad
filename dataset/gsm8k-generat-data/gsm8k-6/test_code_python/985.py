def solution():
    # Calculate the number of pages that are crumpled or blurred
    crumpled_pages = 6  # every seventh page is crumpled, so 1 out of 7 pages is affected
    blurred_pages = 14  # every third page is blurred, so 1 out of 3 pages is affected
    total_crumpled_or_blurred = crumpled_pages + blurred_pages - 2  # pages that are both crumpled and blurred are counted twice

    # Calculate the number of pages that are neither crumpled nor blurred
    total_pages = 42
    neither_crumpled_nor_blurred = total_pages - total_crumpled_or_blurred
    result = neither_crumpled_nor_blurred
    return result

print(solution())