def solution():
    """Zack's number of marbles can be divided equally among three people, leaving Zack with 5. If Zack decided to give his three friends 20 marbles each and kept five, how many marbles did he initially have?"""
    remainder = 5
    marbles_each = 20
    total_marbles_given = marbles_each * 3
    total_marbles = total_marbles_given + remainder
    result = total_marbles
    return result

print(solution())