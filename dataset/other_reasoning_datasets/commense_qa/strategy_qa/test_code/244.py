def solution():
    sea_of_japan_max_depth = 3742
    mount_fuji_height = 3786.24 # convert meters to feet
    if mount_fuji_height > sea_of_japan_max_depth:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())