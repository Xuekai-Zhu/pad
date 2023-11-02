def solution():
    """On Tuesday, Mike had 45 books and Corey had twice as many books as Mike. 
    On Wednesday, Mike gave 10 books to Lily, and Corey gave Lily 15 more than Mike gave.
    How many books did Lily get?"""
    
    # Calculate the number of books Corey had on Tuesday, which is twice the number of books Mike had
    mike_books = 45
    corey_books = mike_books * 2
    
    # Calculate the total number of books Mike gave to Lily on Wednesday
    mike_gave = 10
    
    # Calculate the total number of books Corey gave to Lily on Wednesday, which is 15 more than what Mike gave
    corey_gave = mike_gave + 15
    
    # Calculate the total number of books Lily received
    lily_books = mike_gave + corey_gave
    
    result = lily_books
    return result

print(solution())