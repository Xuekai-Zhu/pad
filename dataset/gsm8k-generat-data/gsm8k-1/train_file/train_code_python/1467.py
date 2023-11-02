def solution():
    """Troy's home is 75 meters away from school while Emily's home is 98 meters away from school. Troy and Emily walk to school and back home every day. How much farther does Emily walk to school and back in five days?"""
    troy_distance = 75 * 2
    emily_distance = 98 * 2
    difference = emily_distance - troy_distance
    total_difference = difference * 5
    result = total_difference
    return result

print(solution())