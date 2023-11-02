def solution():
    # Calculate the total number of picks Johnny has
    blue_picks = 12
    total_picks = blue_picks * 3  # one-third of his picks are blue, so total picks are 3 times the blue picks

    # Calculate the number of red and yellow picks
    red_picks = total_picks / 2  # half of his picks are red
    yellow_picks = total_picks - red_picks - blue_picks  # the rest are yellow

    result = yellow_picks
    return result

print(solution())