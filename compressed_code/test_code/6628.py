def solution():
    
    
    westward_fish = 1800
    eastward_fish = 3200
    northward_fish = 500
    
    east_fish_caught = (2/5) * eastward_fish
    west_fish_caught = (3/4) * westward_fish
    
    total_fish_caught = east_fish_caught + west_fish_caught
    
    total_fish_left = eastward_fish + westward_fish + northward_fish - total_fish_caught
    
    return total_fish_left

print(solution())