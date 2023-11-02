def solution():
    """Joey has 30 pages to read for history class tonight. He decided that he would take a break when he finished reading 70% of the pages assigned. How many pages must he read after he takes a break?"""
    # Define the total number of pages Joey has to read
    total_pages = 30

    # Calculate the number of pages Joey needs to read before taking a break
    pages_before_break = total_pages * 0.7

    # Calculate the number of pages Joey needs to read after taking a break
    pages_after_break = total_pages - pages_before_break

    result = pages_after_break
    return result

print(solution())