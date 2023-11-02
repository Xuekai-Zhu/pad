def solution():
    total_pages = 42
    crumpled_or_blurred_pages = 0

    for page_num in range(1, total_pages + 1):
        if page_num % 7 == 0 or page_num % 3 == 0:
            crumpled_or_blurred_pages += 1

    non_crumpled_non_blurred_pages = total_pages - crumpled_or_blurred_pages
    result = non_crumpled_non_blurred_pages
    return result

print(solution())