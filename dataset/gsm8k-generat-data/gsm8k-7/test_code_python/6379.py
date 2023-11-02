def solution():
    num_letters = 10 # 30 days in a month, Steve writes a letter every 3rd day
    time_per_letter = 20 # in minutes
    time_per_page = 10 # in minutes
    num_pages_regular_letters = num_letters * time_per_letter / time_per_page

    time_long_letter = 80 # in minutes
    time_per_page_long_letter = 2 * time_per_page # in minutes
    num_pages_long_letter = time_long_letter / time_per_page_long_letter

    total_num_pages = num_pages_regular_letters + num_pages_long_letter
    result = total_num_pages
    return result

print(solution())