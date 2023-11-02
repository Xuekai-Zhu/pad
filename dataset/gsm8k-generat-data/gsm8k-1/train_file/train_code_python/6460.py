def solution():
    """John had $200. He gave 3/8 of his money to his mother and 3/10 to his father. How much money did John have left?"""
    total_money = 200
    mother_share = total_money * (3/8)
    father_share = total_money * (3/10)
    john_left = total_money - mother_share - father_share
    result = john_left
    return result

print(solution())