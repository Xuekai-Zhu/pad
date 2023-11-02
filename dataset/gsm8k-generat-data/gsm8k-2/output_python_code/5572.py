def solution():
    """Amy bakes muffins for her friends. On Monday, she brings 1 muffin to school to share. Each day for the rest of the week she brings one more muffin to school than she did the day before. If on Saturday she counts that there are 7 muffins left, how many did she originally bake?"""
    total_muffins_left = 7
    muffins_per_day = [1, 2, 3, 4, 5, 6, 7]
    total_muffins = sum(muffins_per_day) + total_muffins_left
    result = total_muffins
    return result

print(solution())