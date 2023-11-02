def solution():
    """On Tuesday, Mike had 45 books and Corey had twice as many books as Mike. On Wednesday, Mike gave 10 books to Lily, and Corey gave Lily 15 more than Mike gave. How many books did Lily get?"""
    # Calculate the initial number of books each person had on Tuesday
    mike_books = 45
    corey_books = 2 * mike_books
    
    # Calculate how many books were given to Lily on Wednesday
    lily_books = 0
    mike_books -= 10
    lily_books += 10
    corey_books -= (10 + 15)
    lily_books += (10 + 15)
    
    # Return the total number of books Lily received
    result = lily_books
    return result

print(solution())