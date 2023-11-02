def solution():
    jane_bread = 90 * 0.75
    wanda_bread = 90 * 3
    total_bread = jane_bread + wanda_bread
    wanda_treats = 90 / 2
    jane_treats = wanda_treats * 0.75
    total_treats = wanda_treats + jane_treats
    total_pieces = total_bread + total_treats
    
    return total_pieces

print(solution())