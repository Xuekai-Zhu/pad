def solution():
    """The new pad of paper has 120 pages. Sammy uses 25% of the pages for his science project, and another 10 pages for his math homework. How many pages remain in the pad?"""
    # Define the total number of pages in the pad
    total_pages = 120

    # Calculate the number of pages used for the science project
    science_pages = total_pages * 0.25

    # Calculate the number of pages remaining after the science project
    remaining_pages = total_pages - science_pages

    # Calculate the number of pages used for math homework
    math_pages = 10

    # Calculate the final number of pages remaining
    final_pages = remaining_pages - math_pages
    
    result = final_pages
    return result

print(solution())