def solution():
    # Find the number of pink daisies
    pink_daisies = 9 * 6  # nine times as many pink daisies as white daisies

    # Find the number of red daisies
    red_daisies = (4 * pink_daisies) - 3  # three less than four times as many red daisies as pink daisies

    # Find the total number of daisies
    total_daisies = 6 + pink_daisies + red_daisies  # 6 white daisies plus pink daisies plus red daisies
    result = total_daisies
    return result

print(solution())