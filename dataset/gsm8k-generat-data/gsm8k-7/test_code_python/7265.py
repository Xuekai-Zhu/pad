def solution():
    num_pieces = 60
    michael_share = num_pieces / 2
    paige_share = (num_pieces - michael_share) / 2
    mandy_share = num_pieces - michael_share - paige_share
    result = mandy_share
    return result

print(solution())