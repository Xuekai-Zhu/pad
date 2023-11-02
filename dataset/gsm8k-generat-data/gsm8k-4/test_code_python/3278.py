def solution():
    """On Tuesday, Mike had 45 books and Corey had twice as many books as Mike. On Wednesday, Mike gave 10 books to Lily, and Corey gave Lily 15 more than Mike gave. How many books did Lily get?"""
    # Define the initial number of books for Mike and Corey
    mike_books = 45
    corey_books = 2 * mike_books

    # Mike gives 10 books to Lily on Wednesday
    mike_books -= 10

    # Corey gives Lily 15 more books than Mike on Wednesday
    corey_books -= (10 + 15)

    # Total number of books Lily received
    lily_books = 10 + 25

    # return the result
    result = lily_books
    return result

print(solution())