def solution():
    # Calculate the total number of chocolate and M&M pieces
    chocolate_chips = 108
    mms = chocolate_chips / 3
    total_pieces = chocolate_chips + mms

    # Calculate the average number of pieces per cookie
    cookies = 48
    pieces_per_cookie = total_pieces / cookies
    result = pieces_per_cookie
    return result

print(solution())