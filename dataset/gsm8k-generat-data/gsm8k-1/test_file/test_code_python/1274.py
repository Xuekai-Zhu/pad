def solution():
    """Tom found 214 seashells, Nancy found 432 seashells, and Benny found 86 seashells on the beach. When they cleaned them, they discovered that 67 were cracked. How many good seashells did they find together?"""
    total_seashells = 214 + 432 + 86
    good_seashells = total_seashells - 67
    result = good_seashells
    return result

print(solution())