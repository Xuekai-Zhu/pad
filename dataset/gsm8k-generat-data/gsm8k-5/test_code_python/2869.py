def solution():
    total_pages = 120  # The pad of paper has 120 pages
    science_pages = total_pages * 0.25  # Sammy uses 25% of the pages for his science project
    math_pages = 10  # Sammy uses 10 pages for his math homework

    # Calculate the number of pages that remain in the pad
    remaining_pages = total_pages - science_pages - math_pages
    result = remaining_pages
    return result

print(solution())