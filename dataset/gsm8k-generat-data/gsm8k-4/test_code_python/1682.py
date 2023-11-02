def solution():
    """John is a hack author. He writes a book every 2 months. He has been writing for 20 years and has earned an average of $30,000 per book. How much money has he made writing?"""
    # Calculate the total number of books John has written
    num_books = 20 * 12 / 2

    # Calculate the total amount of money John has earned
    total_money = num_books * 30000

    # return the result
    result = total_money
    return result

print(solution())