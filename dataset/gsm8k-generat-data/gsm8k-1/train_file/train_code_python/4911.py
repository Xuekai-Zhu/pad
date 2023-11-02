def solution():
    """Joey has 30 pages to read for history class tonight. He decided that he would take a break when he finished reading 70% of the pages assigned. How many pages must he read after he takes a break?"""
    total_pages = 30
    percent_to_read = 70
    percent_decimal = percent_to_read / 100
    pages_to_read_before_break = total_pages * percent_decimal
    pages_after_break = total_pages - pages_to_read_before_break
    result = pages_after_break
    return result

print(solution())