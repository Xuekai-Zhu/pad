def solution():
    muffins_left_on_sat = 7  # Amy counts 7 muffins left on Saturday
    muffins_per_day = 1  # Amy brings 1 muffin to school on Monday
    days = 6  # Amy brings muffins for 6 days (Tuesday-Saturday)

    # Calculate the total number of muffins Amy brought to school for the week
    total_muffins = muffins_per_day
    for i in range(1, days+1):
        total_muffins += muffins_per_day + i

    # Calculate the original number of muffins Amy baked
    original_num_muffins = total_muffins + muffins_left_on_sat
    result = original_num_muffins
    return result

print(solution())