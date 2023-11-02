def solution():
    mount_everest_elevation = 8848
    mount_emei_elevation = 3099
    if mount_everest_elevation > mount_emei_elevation:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())