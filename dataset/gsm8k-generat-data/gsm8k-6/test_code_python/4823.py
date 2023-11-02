def solution():
    # Calculate the total number of fires put out by the three firefighters
    doug_fires = 20
    kai_fires = 3 * doug_fires
    eli_fires = kai_fires / 2
    total_fires = doug_fires + kai_fires + eli_fires
    result = total_fires
    return result

print(solution())