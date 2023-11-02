def solution():
    # Calculate the number of regular letters Steve writes in a month
    num_regular_letters = 30 // 3
    time_per_regular_letter = 20 / num_regular_letters
    num_pages_per_regular_letter = time_per_regular_letter / 10

    # Calculate the number of pages in Steve's long letter
    time_per_long_letter = 80
    time_per_page_long_letter = time_per_long_letter / num_pages_per_regular_letter / 2

    # Calculate the total number of pages Steve writes in a month
    total_pages = num_regular_letters * num_pages_per_regular_letter + time_per_long_letter / time_per_page_long_letter
    result = total_pages
    return result

print(solution())