def solution():
    """Johnny is a guitar player and he has three colors of guitar picks: red, blue, and yellow. Half of his picks are red, one-third of the picks are blue,
    and the rest are yellow. If he has 12 blue picks, what is the total number of yellow picks in his collection?"""
    # Calculate the total number of picks
    total_picks = 12 / (1/3) # Since one-third of the picks are blue, and Johnny has 12 blue picks, the total number of picks = 3 * 12 = 36

    # Calculate the number of red picks
    red_picks = total_picks / 2

    # Calculate the number of yellow picks
    yellow_picks = total_picks - red_picks - 12 # The rest of the picks are yellow, so we subtract the number of red and blue picks

    # Display the total number of yellow picks
    result = yellow_picks
    return result

print(solution())