def solution():
    """ Joey has 30 pages to read for history class tonight. He decided that he would take a break when he finished reading 70% of the pages assigned. How many pages must he read after he takes a break?"""
    # Define the total number of pages to read and the percentage to be read before the break
    total_pages = 30
    percentage_before_break = 0.7

    # Calculate the number of pages to read before the break
    pages_before_break = total_pages * percentage_before_break

    # Calculate the number of pages to read after the break
    pages_after_break = total_pages - pages_before_break

    # Display the number of pages to read after the break
    result = pages_after_break
    return result

print(solution())