def solution():
    """Lana had 8 blank pages left in her binder, but she knew she would need more for her next class. Duane took half of the 42 pages in his binder out and gave them to her. How many pages does Lana have in her binder after adding Duane’s?"""
    # Define the number of pages in Duane's binder
    DUANE_PAGES = 42

    # Calculate the number of pages Duane gave to Lana
    pages_given = DUANE_PAGES / 2

    # Calculate the total number of pages Lana has after adding Duane's
    total_pages = 8 + pages_given

    # Display the total number of pages
    result = total_pages
    return result

print(solution())