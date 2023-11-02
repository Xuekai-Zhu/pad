def solution():
    """Zack's number of marbles can be divided equally among three people, leaving Zack with 5. If Zack decided to give his three friends 20 marbles each and kept five, how many marbles did he initially have?"""
    marbles_remainder = 5
    friends_marbles = 20 * 3
    total_marbles = marbles_remainder + friends_marbles
    initial_marbles = total_marbles * 3
    result = initial_marbles
    return result

print(solution())