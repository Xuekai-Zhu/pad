def solution():
    """At the bookstore, Sarah bought 6 paperback books and 4 hardback books. Her brother bought one-third as many paperback books as Sarah bought, and two times the number of hardback books that she bought. How many books did her brother buy in total?"""
    sarah_paperback = 6
    sarah_hardback = 4
    brother_paperback = sarah_paperback / 3
    brother_hardback = sarah_hardback * 2
    total_books = sarah_paperback + sarah_hardback + brother_paperback + brother_hardback
    result = total_books
    return result

print(solution())