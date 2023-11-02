def solution():
    # Find the total number of chocolate pieces and M&Ms in the batch
    total_pieces = 108 + (1/3 * 108)  # adding one-third of the chocolate chips for the M&Ms

    # Find the average number of chocolate pieces per cookie
    avg_pieces_per_cookie = total_pieces / 48
    result = avg_pieces_per_cookie
    return result

print(solution())