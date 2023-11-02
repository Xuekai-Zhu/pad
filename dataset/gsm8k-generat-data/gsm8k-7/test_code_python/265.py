def solution():
    barry_reach = 5  # in feet
    larry_height = 5  # in feet
    larry_shoulder_height = larry_height * 0.8  # 20% less than full height

    total_reach = barry_reach + larry_shoulder_height
    result = total_reach
    return result

print(solution())