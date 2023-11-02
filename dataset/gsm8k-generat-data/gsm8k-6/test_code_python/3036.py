def solution():
    # Calculate the number of books that can be sold for $2.50 each and $2 each
    num_expensive_books = (2/5) * 10  
    num_cheap_books = 10 - num_expensive_books

    # Calculate the total amount of money Lovely can earn
    total_money = (num_expensive_books * 2.5) + (num_cheap_books * 2)
    result = total_money
    return result

print(solution())