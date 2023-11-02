def solution():
    """Steve writes a letter every 3rd day to his friend.  He spends 20 minutes writing the letters. 
    It takes 10 minutes to write 1 page.  He also writes a long letter at the end of the month 
    which he puts more thought into.  It takes twice as long per page but he spends 80 minutes writing. 
    How many pages does he write a month?"""
    # Define the time it takes to write a normal letter and a long letter
    NORMAL_LETTER_TIME = 20
    LONG_LETTER_TIME = 80

    # Define the time it takes to write a page
    PAGE_TIME = 10

    # Calculate the total number of normal letters written in a month
    normal_letters = 30 // 3  # Divide 30 (number of days in a month) by 3 (days between letters)
    normal_pages = normal_letters  # Each normal letter is one page

    # Calculate the number of pages in the long letter
    long_pages = (LONG_LETTER_TIME / PAGE_TIME) * 2

    # Calculate the total number of pages written in a month
    total_pages = normal_pages + long_pages

    # Display the total number of pages
    result = int(total_pages)  # Convert to integer for readability
    return result

print(solution())