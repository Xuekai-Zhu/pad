def solution():
    """Milton has some books about zoology and 4 times as many books about botany. If he has 80 books total, how many zoology books does he have?"""
    # Define the number of books about botany relative to zoology
    botany_to_zoology_ratio = 4

    # Define the total number of books
    total_books = 80

    # Calculate the total number of books about botany
    botany_books = total_books / (botany_to_zoology_ratio + 1) * botany_to_zoology_ratio

    # Calculate the number of books about zoology
    zoology_books = total_books - botany_books

    # Return the result
    result = zoology_books
    return result

print(solution())