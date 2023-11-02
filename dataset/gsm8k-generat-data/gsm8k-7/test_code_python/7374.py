def solution():
    num_whole_pies = 4
    num_pies_sold = 1
    num_pies_given_away = 1
    num_pies_left = num_whole_pies - num_pies_sold - num_pies_given_away

    # Calculate the total number of pieces of pie
    total_num_pieces = num_pies_left * 6

    # Calculate the number of pieces eaten by Grace's family
    num_pieces_eaten = (2/3) * total_num_pieces

    # Calculate the number of pieces of pie left
    num_pieces_left = total_num_pieces - num_pieces_eaten
    result = num_pieces_left
    return result

print(solution())