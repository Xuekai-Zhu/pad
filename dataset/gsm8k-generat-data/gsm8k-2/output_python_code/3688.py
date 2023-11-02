def solution():
    """Johnny is a guitar player and he has three colors of guitar picks: red, blue, and yellow. Half of his picks are red, one-third of the picks are blue, and the rest are yellow. If he has 12 blue picks, what is the total number of yellow picks in his collection?"""
    blue_picks = 12
    total_picks = blue_picks / (1/3) #(1/3) is the proportion of blue picks in the collection
    red_picks = (1/2) * total_picks #(1/2) is the proportion of red picks in the collection
    yellow_picks = total_picks - blue_picks - red_picks #The rest of the picks are yellow
    result = yellow_picks
    return result

print(solution())