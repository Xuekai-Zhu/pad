def solution():
    black_socks = 6  # given
    white_socks = 4 * black_socks  # Andy has 4 times as many white socks as black socks
    white_socks_after_loss = 0.5 * white_socks  # Andy loses half of his white socks
    remaining_white_socks = white_socks - white_socks_after_loss  # white socks remaining after loss
    diff_white_black = remaining_white_socks - black_socks  # difference between remaining white socks and black socks
    result = diff_white_black
    return result

print(solution())