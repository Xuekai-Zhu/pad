def solution():
    whole_pies = 4  # Grace baked 4 whole pumpkin pies
    sold_pies = 1  # Grace sold 1 whole pumpkin pie
    given_pies = 1  # Grace gave 1 whole pumpkin pie to her friend

    # Calculate the number of remaining whole pumpkin pies
    remaining_pies = whole_pies - sold_pies - given_pies

    # Calculate the total number of pumpkin pie pieces
    total_pieces = remaining_pies * 6

    # Calculate the number of pumpkin pie pieces eaten by Grace's family
    eaten_pieces = (2/3) * total_pieces

    # Calculate the number of pumpkin pie pieces left
    remaining_pieces = total_pieces - eaten_pieces
    result = remaining_pieces
    return result

print(solution())