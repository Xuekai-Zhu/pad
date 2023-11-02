def solution():
    
    westward_fish = 1800
    eastward_fish = 3200
    northward_fish = 500
    caught_eastward_fish = 2/5 * eastward_fish
    caught_westward_fish = 3/4 * westward_fish
    remaining_fish = westward_fish - caught_westward_fish + eastward_fish - caught_eastward_fish + northward_fish
    result = remaining_fish
    return result

print(solution())