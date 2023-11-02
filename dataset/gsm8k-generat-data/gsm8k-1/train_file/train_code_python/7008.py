def solution():
    """Pablo’s mother agrees to pay him one cent for every page he reads. He plans to save the money for some candy. 
    Pablo always checks out books that are exactly 150 pages. After reading his books, he went to the store and bought $15 
    worth of candy and had $3 leftover. How many books did Pablo read?"""
    candy_cost = 15
    leftover_money = 3
    money_earned = (candy_cost + leftover_money) * 100  # converting dollars to cents
    pages_read = money_earned / 150  # each book is 150 pages
    books_read = int(pages_read / 1)  # rounding down to the nearest book
    result = books_read
    return result

print(solution())