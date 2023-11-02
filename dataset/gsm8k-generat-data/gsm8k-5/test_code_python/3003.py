def solution():
    depth_in_june = 45/3 - 10  # depth in July is three times deeper than in June and 10 feet deeper than in May
    depth_in_may = depth_in_june - 10  # depth in June is 10 feet deeper than in May

    return depth_in_may

print(solution())