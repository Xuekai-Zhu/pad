def solution():
    """Lana had 8 blank pages left in her binder, but she knew she would need more for her next class. Duane took half of the 42 pages in his binder out and gave them to her. How many pages does Lana have in her binder after adding Duane’s?"""
    # Define the initial number of pages in Lana's binder
    lana_pages = 8

    # Define the number of pages in Duane's binder
    duane_pages = 42

    # Calculate the number of pages Duane gives to Lana
    duane_gives = duane_pages / 2

    # Add the pages to Lana's binder
    total_pages = lana_pages + duane_gives

    # Return the result
    result = total_pages
    return result

print(solution())