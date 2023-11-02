def solution():
    # Define the number of blue picks and the fraction of picks that are blue
    blue_picks = 12
    blue_fraction = 1/3

    # Calculate the total number of picks
    total_picks = blue_picks / blue_fraction

    # Calculate the number of red picks and yellow picks
    red_picks = total_picks / 2
    yellow_picks = total_picks - blue_picks - red_picks

    result = yellow_picks
    return result

print(solution())