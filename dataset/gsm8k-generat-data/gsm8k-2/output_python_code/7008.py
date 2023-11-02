def solution():
    """Pablo’s mother agrees to pay him one cent for every page he reads. He plans to save the money for some candy. Pablo always checks out books that are exactly 150 pages. After reading his books, he went to the store and bought $15 worth of candy and had $3 leftover. How many books did Pablo read?"""
    candy_cost = 15
    leftover_money = 3
    total_money = (candy_cost + leftover_money) * 100  # convert dollars to cents
    book_pages = 150
    book_pay = book_pages * 0.01
    total_books = total_money // book_pay
    result = total_books
    return result

print(solution())