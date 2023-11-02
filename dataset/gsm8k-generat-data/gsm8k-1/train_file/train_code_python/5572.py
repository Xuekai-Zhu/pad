def solution():
    """Amy bakes muffins for her friends. On Monday, she brings 1 muffin to school to share. Each day for the rest of the week she brings one more muffin to school than she did the day before. If on Saturday she counts that there are 7 muffins left, how many did she originally bake?"""
    muffins_left_on_saturday = 7
    muffins_baked_on_monday = 1
    total_muffins = muffins_baked_on_monday
    for i in range(1, 6):
        muffins_baked_on_day_i = muffins_baked_on_monday + i
        total_muffins += muffins_baked_on_day_i
    muffins_baked_orig = total_muffins + muffins_left_on_saturday
    result = muffins_baked_orig
    return result

print(solution())