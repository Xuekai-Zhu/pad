def solution():
    # Calculate the number of pages Cora needs to read on Thursday to finish the book by Friday
    pages_left = 158 - 23 - 38 - 61  # subtract the pages already read from the total pages
    friday_pages = 2 * thursday_pages  # Cora will read twice as much on Friday as she does on Thursday
    pages_left -= friday_pages  # subtract Friday's pages from the pages left
    thursday_pages = pages_left / 2  # divide the remaining pages equally between Thursday and Friday
    result = thursday_pages
    return result

print(solution())