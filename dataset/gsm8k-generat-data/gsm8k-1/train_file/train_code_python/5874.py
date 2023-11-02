def solution():
    """Lana had 8 blank pages left in her binder, but she knew she would need more for her next class. 
    Duane took half of the 42 pages in his binder out and gave them to her. How many pages does Lana have in her binder after adding Duane’s?"""
    lana_initial_pages = 8
    duane_initial_pages = 42
    duane_gave_pages = duane_initial_pages / 2
    total_pages = lana_initial_pages + duane_gave_pages
    result = total_pages
    return result

print(solution())