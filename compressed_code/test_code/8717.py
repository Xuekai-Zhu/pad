def solution():
    
    total_cookies = 48
    chocolate_chips = 108
    m_and_ms = chocolate_chips / 3
    total_chocolate_pieces = chocolate_chips + m_and_ms
    average_chocolate_pieces_per_cookie = total_chocolate_pieces / total_cookies
    result = average_chocolate_pieces_per_cookie
    return result

print(solution())