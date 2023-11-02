def solution():
    sarah_pb = 6  # Sarah bought 6 paperback books
    sarah_hb = 4  # Sarah bought 4 hardback books
    brother_pb = sarah_pb / 3  # Her brother bought one-third as many paperback books
    brother_hb = 2 * sarah_hb  # Her brother bought two times the number of hardback books
    total_books_brother = brother_pb + brother_hb  # Total number of books purchased by Sarah's brother
    result = total_books_brother
    return result

print(solution())