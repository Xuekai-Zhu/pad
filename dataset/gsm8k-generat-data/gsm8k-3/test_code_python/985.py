def solution():
    """James has an old printer that crumples every seventh page and blurs the ink on every third page. If he prints 42 pages, how many are neither crumpled or blurred?"""
    # Define the total number of pages James prints
    total_pages = 42

    # Define the number of pages that are crumpled or blurred
    crumpled_pages = total_pages // 7
    blurred_pages = total_pages // 3

    # Define the number of pages that are crumpled and blurred
    common_pages = total_pages // (3*7)

    # Calculate the number of pages that are neither crumpled nor blurred
    non_crumpled_or_blurred = total_pages - (crumpled_pages + blurred_pages - common_pages)

    # Display the number of pages that are neither crumpled nor blurred
    result = non_crumpled_or_blurred
    return result

print(solution())