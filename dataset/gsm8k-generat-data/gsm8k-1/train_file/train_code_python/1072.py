def solution():
    """1,800 fish swim westward, 3,200 swim eastward, and 500 swim north. What is the number of fish left in the sea,
    if fishers catch 2/5 of the fish that swam eastward and 3/4 of the fish that swam westward?"""
    
    westward_fish = 1800
    eastward_fish = 3200
    northward_fish = 500
    
    east_fish_caught = (2/5) * eastward_fish
    west_fish_caught = (3/4) * westward_fish
    
    total_fish_caught = east_fish_caught + west_fish_caught
    
    total_fish_left = eastward_fish + westward_fish + northward_fish - total_fish_caught
    
    return total_fish_left

print(solution())