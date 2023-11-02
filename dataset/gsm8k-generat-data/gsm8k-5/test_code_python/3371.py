def solution():
    total_pages = 95  # The book has 95 pages in total
    num_chapters = 5  # The book has 5 chapters

    # Use algebra to solve for the number of pages in the first chapter
    # Let x be the number of pages in the first chapter
    # Then the number of pages in the second chapter is x + 3
    # The number of pages in the third chapter is x + 6, and so on
    # The sum of the number of pages in all 5 chapters is 95
    # Therefore, we have: x + (x+3) + (x+6) + (x+9) + (x+12) = 95
    # Simplifying, we get: 5x + 30 = 95
    # Solving for x, we get: x = 13

    # Therefore, the first chapter has 13 pages
    result = 13
    return result

print(solution())