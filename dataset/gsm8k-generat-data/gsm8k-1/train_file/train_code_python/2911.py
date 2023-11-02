def solution():
    """Alex is stacking his books in a pyramid. Each level of the pyramid has 80% as many books as the number of books in the previous level.
    If he makes four levels and the top level has 64 books, how many books are in the pyramid in total?"""
    top_level = 64
    previous_level = top_level / 0.8
    second_level = previous_level / 0.8
    third_level = second_level / 0.8
    total_books = top_level + previous_level + second_level + third_level
    result = total_books
    return result

print(solution())