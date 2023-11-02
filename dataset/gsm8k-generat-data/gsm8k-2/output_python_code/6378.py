def solution():
    """Steve writes a letter every 3rd day to his friend. He spends 20 minutes writing the letters. It takes 10 minutes to write 1 page. He also writes a long letter at the end of the month which he puts more thought into. It takes twice as long per page but he spends 80 minutes writing. How many pages does he write a month?"""
    regular_letters_days = 30//3 # Every 3rd day
    regular_letters_time = regular_letters_days * 20
    regular_letters_pages = regular_letters_time // 10
    
    long_letter_pages = (80 // 20) * 2  # Twice as long as regular letters
    total_pages = regular_letters_pages + long_letter_pages
    result = total_pages
    return result

print(solution())