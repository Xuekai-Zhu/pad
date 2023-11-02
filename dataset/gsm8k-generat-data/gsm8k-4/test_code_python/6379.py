def solution():
    """Steve writes a letter every 3rd day to his friend. He spends 20 minutes writing the letters. It takes 10 minutes to write 1 page. He also writes a long letter at the end of the month which he puts more thought into. It takes twice as long per page but he spends 80 minutes writing. How many pages does he write a month?"""
    # Define the number of letters Steve writes in a month
    letters_per_month = 30 // 3

    # Calculate the total time spent writing the regular letters
    time_regular_letters = letters_per_month * 20

    # Calculate the number of pages written in the regular letters
    pages_regular_letters = time_regular_letters // 10

    # Calculate the time spent writing the long letter
    time_long_letter = 80

    # Calculate the number of pages written in the long letter
    pages_long_letter = (time_long_letter / 2) // 10

    # Calculate the total number of pages written in a month
    total_pages = pages_regular_letters + pages_long_letter

    result = total_pages
    return result

print(solution())