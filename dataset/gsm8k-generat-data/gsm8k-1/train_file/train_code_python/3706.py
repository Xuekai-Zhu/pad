def solution():
    """Colleen is making a batch of 48 cookies. She's going to add 108 chocolate chips and one-third as many M&Ms to the whole batch. What are the average number of chocolate pieces in each cookie?"""
    total_cookies = 48
    chocolate_chips = 108
    m_and_ms = chocolate_chips / 3
    total_chocolate_pieces = chocolate_chips + m_and_ms
    average_chocolate_pieces_per_cookie = total_chocolate_pieces / total_cookies
    result = average_chocolate_pieces_per_cookie
    return result

print(solution())