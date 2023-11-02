def solution():
    num_books = 10
    num_expensive_books = num_books * (3/5)  # Two-fifths can be sold for $2.50, so three-fifths are left to be sold at $2 each
    total_earned = (num_expensive_books * 2.5) + ((num_books - num_expensive_books) * 2)
    result = total_earned
    return result

print(solution())