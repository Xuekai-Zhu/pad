def solution():
    # Calculate the total number of muffins Amy brought to school throughout the week
    total_muffins = 1 + 2 + 3 + 4 + 5 + 6  # she brings one more muffin each day from Monday to Saturday
    # Calculate the total number of muffins she originally baked
    original_muffins = total_muffins + 7  # there are 7 muffins left on Saturday
    result = original_muffins
    return result

print(solution())