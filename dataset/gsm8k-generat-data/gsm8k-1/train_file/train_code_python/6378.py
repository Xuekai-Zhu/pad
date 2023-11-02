def solution():
    """Steve writes a letter every 3rd day to his friend. He spends 20 minutes writing the letters.
    It takes 10 minutes to write 1 page. He also writes a long letter at the end of the month which he puts more thought into.
    It takes twice as long per page but he spends 80 minutes writing. How many pages does he write a month?"""
    
    days_per_month = 30
    letters_per_month = days_per_month // 3
    pages_per_letter = 2
    regular_letters_pages = letters_per_month * pages_per_letter
    regular_letters_time = letters_per_month * 20
    
    long_letter_pages = (80 - regular_letters_time) // 20 * 2
    
    total_pages = regular_letters_pages + long_letter_pages
    result = total_pages
    return result

print(solution())