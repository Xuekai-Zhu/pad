def solution():
    eggs_per_dozen = 12  # There are 12 eggs in a dozen
    eggs_to_store_1 = 5 * eggs_per_dozen  # Mark supplies 5 dozen eggs to store 1
    eggs_to_store_2 = 30  # Mark supplies 30 eggs to store 2
    days_per_week = 7  # There are 7 days in a week

    # Calculate the total number of eggs supplied in a week
    total_eggs = (eggs_to_store_1 + eggs_to_store_2) * days_per_week
    result = total_eggs
    return result

print(solution())