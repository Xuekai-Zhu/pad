def solution():
    """Troy's home is 75 meters away from school while Emily's home is 98 meters away from school. Troy and Emily walk to school and back home every day. How much farther does Emily walk to school and back in five days?"""
    troy_distance = 2 * 75
    emily_distance = 2 * 98
    emily_extra_distance = emily_distance - troy_distance
    total_emily_extra_distance = emily_extra_distance * 5
    result = total_emily_extra_distance
    return result

print(solution())