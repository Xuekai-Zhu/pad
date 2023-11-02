def solution():
    """I have purchased 5 blue apples at the store. Suppose my neighbor gives me twice as many yellow apples as I have blue ones, and then I give my son 1/5 of the total number of apples; how many apples do I have now?"""
    blue_apples = 5
    yellow_apples = 2 * blue_apples
    total_apples = blue_apples + yellow_apples
    son_apples = total_apples / 5
    remaining_apples = total_apples - son_apples
    result = remaining_apples
    return result

print(solution())