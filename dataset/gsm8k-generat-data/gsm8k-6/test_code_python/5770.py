def solution():
    # Calculate the total number of eggs supplied in a week
    eggs_per_day = (5*12) + 30  # 5 dozen eggs to one store and 30 eggs to another store
    total_eggs = eggs_per_day * 7  # number of days in a week
    result = total_eggs
    return result

print(solution())