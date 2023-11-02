def solution():
    guppies = 94
    angelfish = 76
    tiger_sharks = 89
    oscar_fish = 58
    sold_guppies = 30
    sold_angelfish = 48
    sold_tiger_sharks = 17
    sold_oscar_fish = 24
    remaining_guppies = guppies - sold_guppies
    remaining_angelfish = angelfish - sold_angelfish
    remaining_tiger_sharks = tiger_sharks - sold_tiger_sharks
    remaining_oscar_fish = oscar_fish - sold_oscar_fish
    result = remaining_guppies + remaining_angelfish + remaining_tiger_sharks + remaining_oscar_fish
    return result

print(solution())