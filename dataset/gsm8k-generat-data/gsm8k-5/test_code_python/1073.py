def solution():
    westward_fish = 1800  # number of fish swimming westward
    eastward_fish = 3200  # number of fish swimming eastward
    northward_fish = 500  # number of fish swimming northward

    # calculate number of fish caught by fishers
    eastward_fish_caught = (2/5) * eastward_fish
    westward_fish_caught = (3/4) * westward_fish

    # calculate total number of fish remaining in the sea
    total_fish_remaining = westward_fish + eastward_fish + northward_fish - eastward_fish_caught - westward_fish_caught

    result = total_fish_remaining
    return result

print(solution())