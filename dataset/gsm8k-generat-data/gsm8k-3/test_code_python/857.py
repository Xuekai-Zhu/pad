def solution():
    """At the bookstore, Sarah bought 6 paperback books and 4 hardback books. Her brother bought one-third as many paperback books as Sarah bought, and two times the number of hardback books that she bought. How many books did her brother buy in total?"""
    # Define the number of paperback and hardback books Sarah bought
    sarah_paperback = 6
    sarah_hardback = 4

    # Calculate the number of paperback and hardback books Sarah's brother bought
    brother_paperback = sarah_paperback // 3
    brother_hardback = sarah_hardback * 2

    # Calculate the total number of books Sarah's brother bought
    total_books = brother_paperback + brother_hardback

    # Display the total number of books
    result = total_books
    return result

print(solution())