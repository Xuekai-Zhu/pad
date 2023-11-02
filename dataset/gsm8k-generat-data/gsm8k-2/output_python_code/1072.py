def solution():
    """1,800 fish swim westward, 3,200 swim eastward, and 500 swim north. What is the number of fish left in the sea, if fishers catch 2/5 of the fish that swam eastward and 3/4 of the fish that swam westward?"""
    westward_fish = 1800
    eastward_fish = 3200
    northward_fish = 500
    caught_eastward_fish = 2/5 * eastward_fish
    caught_westward_fish = 3/4 * westward_fish
    remaining_fish = westward_fish - caught_westward_fish + eastward_fish - caught_eastward_fish + northward_fish
    result = remaining_fish
    return result

print(solution())