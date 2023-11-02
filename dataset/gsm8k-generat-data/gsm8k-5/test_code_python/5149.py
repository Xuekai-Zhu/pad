def solution():
    # Calculate the total number of fish in the tank
    total_fish = 94 + 76 + 89 + 58

    # Calculate the number of fish sold
    guppies_sold = 30
    angelfish_sold = 48
    tiger_sharks_sold = 17
    oscar_fish_sold = 24

    # Calculate the remaining number of fish in the tank
    remaining_guppies = 94 - guppies_sold
    remaining_angelfish = 76 - angelfish_sold
    remaining_tiger_sharks = 89 - tiger_sharks_sold
    remaining_oscar_fish = 58 - oscar_fish_sold
    remaining_fish = remaining_guppies + remaining_angelfish + remaining_tiger_sharks + remaining_oscar_fish

    result = remaining_fish
    return result

print(solution())