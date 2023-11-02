def solution():
    # Calculate the total number of pages Mitchell had read before 4 o'clock
    pages_before_4 = 10 * 40

    # Calculate the total number of pages Mitchell had read after 4 o'clock
    pages_after_4 = (2 * 40) + 20  # Mitchell read 2 more chapters of 40 pages each, and also 20 pages from chapter 11

    # Calculate the total number of pages Mitchell had read altogether
    total_pages = pages_before_4 + pages_after_4
    result = total_pages
    return result

print(solution())