def solution():
    # Calculate the depth of the river in mid-May
    x = 10  # difference between mid-May and mid-June
    y = 3 * x  # difference between mid-June and mid-July
    z = y + x  # depth of the river in mid-July
    depth_may = z - 45  # depth of the river in mid-May
    result = depth_may
    return result

print(solution())