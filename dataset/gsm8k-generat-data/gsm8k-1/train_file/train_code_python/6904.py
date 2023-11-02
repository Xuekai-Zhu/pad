def solution():
    """Peter has 20 books. He has read 40% of them. His brother has read 10% of them. How many more of these books has Peter read than his brother?"""
    total_books = 20
    peter_read = total_books * 0.4
    brother_read = total_books * 0.1
    difference = peter_read - brother_read
    result = difference
    return result

print(solution())