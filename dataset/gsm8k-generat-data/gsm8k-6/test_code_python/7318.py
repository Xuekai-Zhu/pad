def solution():
    # Calculate the total number of purple and orange pages read by Mirella
    purple_pages = 5 * 230  # each purple book has 230 pages and Mirella read 5 purple books
    orange_pages = 4 * 510  # each orange book contains 510 pages and Mirella read 4 orange books

    # Calculate the difference in the number of orange and purple pages read
    difference = orange_pages - purple_pages
    result = difference
    return result

print(solution())