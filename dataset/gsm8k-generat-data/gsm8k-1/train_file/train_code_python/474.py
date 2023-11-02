def solution():
    """Maggie picked 40 apples. Kelsey picked 28 apples. Layla picked some apples, too. The three averaged 30 apples picked. How many did Layla pick?"""
    total_apples = 40 + 28
    average_apples = 30
    layla_apples = (3 * average_apples) - total_apples
    result = layla_apples
    return result

print(solution())