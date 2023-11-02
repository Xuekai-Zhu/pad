def solution():
    # Calculate the area Tommy can ride in
    tommy_area = (2 + 2) * (3 + 1)  # 2 blocks north, 3 blocks east, 2 blocks west, 2 blocks south

    # Calculate the area Tommy's friend can ride in
    friend_area = 80

    # Calculate the ratio of the areas
    area_ratio = friend_area / tommy_area
    result = area_ratio
    return result

print(solution())