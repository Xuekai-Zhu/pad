def solution():
    """Ted starts with $200. He buys 3 books for 16 dollars each and 3 pencils for 6 dollars each. How much did he spend in total?"""
    starting_amount = 200
    num_books = 3
    book_price = 16
    num_pencils = 3
    pencil_price = 6
    total_spent = starting_amount - (num_books * book_price) - (num_pencils * pencil_price)
    result = total_spent
    return result

print(solution())