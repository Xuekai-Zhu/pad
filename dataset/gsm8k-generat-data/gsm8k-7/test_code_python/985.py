def solution():
    num_pages = 42

    # Calculate the number of crumpled pages
    num_crumpled = num_pages // 7

    # Calculate the number of blurred pages
    num_blurred = num_pages // 3

    # Calculate the number of pages that are both crumpled and blurred (every 21st page)
    num_crumpled_blurred = num_pages // 21

    # Calculate the total number of pages that are either crumpled or blurred
    total_crumpled_blurred = num_crumpled + num_blurred - num_crumpled_blurred

    # Calculate the number of pages that are neither crumpled nor blurred
    num_neither = num_pages - total_crumpled_blurred
    result = num_neither
    return result

print(solution())