def solution():
    blue_picks = 12
    red_ratio = 1/2
    blue_ratio = 1/3

    # Calculate the total number of picks
    total_picks = blue_picks / blue_ratio

    # Calculate the number of red picks
    red_picks = total_picks * red_ratio

    # Calculate the number of yellow picks
    yellow_picks = total_picks - blue_picks - red_picks
    result = yellow_picks
    return result

print(solution())