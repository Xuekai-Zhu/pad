def solution():
    depth_increase_may_june = 10
    depth_increase_june_july = depth_increase_may_june * 3
    depth_july = 45
    depth_june = depth_july - depth_increase_june_july
    depth_may = depth_june - depth_increase_may_june
    result = depth_may
    return result

print(solution())