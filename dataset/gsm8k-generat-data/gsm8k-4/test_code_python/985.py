def solution():
    """James has an old printer that crumples every seventh page and blurs the ink on every third page. If he prints 42 pages, how many are neither crumpled or blurred?"""
    # Define the total number of pages to print
    total_pages = 42

    # Define the number of crumpled pages and blurred pages
    crumpled_pages = total_pages // 7
    blurred_pages = total_pages // 3

    # Define the number of pages that are both crumpled and blurred
    crumpled_and_blurred_pages = total_pages // 21

    # Calculate the number of pages that are neither crumpled nor blurred
    neither_crumpled_nor_blurred_pages = total_pages - crumpled_pages - blurred_pages + crumpled_and_blurred_pages

    # return the result
    result = neither_crumpled_nor_blurred_pages
    return result

print(solution())