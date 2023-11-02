def solution():
    total_fish = 66  # There are 66 fish in the tank
    red_stripes = total_fish / 3  # One-third of the fish have red stripes
    remaining_fish = total_fish - red_stripes  # Calculate the number of fish remaining with red stripes
    blue_stripes = (5/11) * remaining_fish  # 5/11 of the remaining fish have blue stripes
    total_red_blue_stripes = red_stripes + blue_stripes  # Calculate the total number of fish with red stripes and blue stripes
    result = total_red_blue_stripes
    return result

print(solution())