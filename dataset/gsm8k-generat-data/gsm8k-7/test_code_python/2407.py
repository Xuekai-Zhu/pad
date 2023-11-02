def solution():
    wanda_bread = 90
    wanda_treats = wanda_bread / 3
    jane_treats = 2 * wanda_treats
    jane_bread = jane_treats * 0.75
    total_bread = wanda_bread + jane_bread
    total_treats = wanda_treats + jane_treats
    result = total_bread + total_treats
    return result

print(solution())