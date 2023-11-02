def solution():
    # Mitchell read 10 chapters, each with 40 pages, before 4 o'clock
    pages_before_4 = 10 * 40

    # Mitchell read 20 pages of chapter 11 after 4 o'clock
    # but didn't finish it, so it doesn't count towards the total
    pages_after_4 = 2 * 40  # Mitchell read 2 more chapters, each with 40 pages

    # Total number of pages Mitchell read altogether
    total_pages_read = pages_before_4 + pages_after_4
    result = total_pages_read
    return result

print(solution())