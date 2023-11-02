def solution():
    blue_picks = 12  # Johnny has 12 blue picks
    blue_percentage = 1/3  # One-third of Johnny's picks are blue
    total_picks = blue_picks / blue_percentage  # Calculate total number of picks using blue percentage
    red_picks = total_picks / 2  # Half of Johnny's picks are red
    yellow_picks = total_picks - blue_picks - red_picks  # The rest of Johnny's picks are yellow
    result = yellow_picks
    return result

print(solution())