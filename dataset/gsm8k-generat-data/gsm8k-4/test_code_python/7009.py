def solution():
    """Pablo’s mother agrees to pay him one cent for every page he reads. He plans to save the money for some candy. Pablo always checks out books that are exactly 150 pages. After reading his books, he went to the store and bought $15 worth of candy and had $3 leftover. How many books did Pablo read?"""
    # Define the amount earned per book
    cents_per_book = 150

    # Define the total amount earned
    total_earned = (15 + 3) * 100

    # Calculate the number of books read
    num_books = total_earned // cents_per_book

    # return the result
    result = num_books
    return result

print(solution())