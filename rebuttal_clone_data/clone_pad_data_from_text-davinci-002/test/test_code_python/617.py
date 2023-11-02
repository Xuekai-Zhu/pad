def solution():
    fish_westward = 1800
    fish_eastward = 3200
    fish_north = 500
    fish_south = 0
    fish_left_west = fish_westward - (fish_westward * 3/4)
    fish_left_east = fish_eastward - (fish_eastward * 2/5)
    fish_left = fish_left_west + fish_left_east + fish_north + fish_south
    result = fish_left
    return result

print(solution())