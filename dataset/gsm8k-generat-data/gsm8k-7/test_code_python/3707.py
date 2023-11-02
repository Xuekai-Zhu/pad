def solution():
    num_cookies = 48
    num_choc_chips = 108
    num_mms = num_choc_chips / 3

    # Calculate the total number of chocolate pieces in the whole batch
    total_choc_pieces = num_choc_chips + num_mms

    # Calculate the average number of chocolate pieces in each cookie
    avg_choc_pieces_per_cookie = total_choc_pieces / num_cookies
    result = avg_choc_pieces_per_cookie
    return result

print(solution())