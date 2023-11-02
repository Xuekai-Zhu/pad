def solution():
    """Johnny is a guitar player and he has three colors of guitar picks: red, blue, and yellow. Half of his picks are red, one-third of the picks are blue, and the rest are yellow.  If he has 12 blue picks, what is the total number of yellow picks in his collection?"""
    # Define the number of blue picks
    blue_picks = 12

    # Calculate the total number of picks
    total_picks = blue_picks * 3

    # Calculate the number of red picks
    red_picks = total_picks / 2

    # Calculate the number of yellow picks
    yellow_picks = total_picks - blue_picks - red_picks

    # return the result
    result = yellow_picks
    return result

print(solution())