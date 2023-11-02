def solution():
    """Colleen is making a batch of 48 cookies. She's going to add 108 chocolate chips and one-third as many M&Ms to the whole batch. What are the average number of chocolate pieces in each cookie?"""
    total_chocolate_chips = 108
    total_mms = total_chocolate_chips / 3
    total_pieces = total_chocolate_chips + total_mms
    cookies = 48
    average_pieces_per_cookie = total_pieces / cookies
    result = average_pieces_per_cookie
    return result

print(solution())