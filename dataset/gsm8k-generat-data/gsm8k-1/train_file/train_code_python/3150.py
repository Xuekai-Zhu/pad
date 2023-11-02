def solution():
    """Jason spent 1/4 of his money and an additional $10 on some books. He then spent 2/5 of the remaining money and an additional $8 on some DVDs. If he was left with $130, how much money did he have at first?"""
    left_at_end = 130
    spent_on_DVDs = 8
    remaining_after_DVDs = left_at_end + spent_on_DVDs
    spent_on_books = 10
    remaining_after_books = remaining_after_DVDs / (3/4) + spent_on_books
    remaining_at_start = remaining_after_books / (3/5)
    total_at_start = remaining_at_start + remaining_after_books
    result = total_at_start
    return result

print(solution())