def solution():
    # Define variables for the number of muffins each day
    monday_muffins = 1
    tuesday_muffins = monday_muffins + 1
    wednesday_muffins = tuesday_muffins + 1
    thursday_muffins = wednesday_muffins + 1
    friday_muffins = thursday_muffins + 1
    saturday_muffins = 7

    # Calculate the total number of muffins baked
    total_muffins = monday_muffins + tuesday_muffins + wednesday_muffins + thursday_muffins + friday_muffins + saturday_muffins

    # Subtract the muffins left on Saturday from the total to get the original number baked
    original_muffins = total_muffins - saturday_muffins

    result = original_muffins
    return result

print(solution())