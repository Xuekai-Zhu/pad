def solution():
    total_puppies = 7
    total_portions = 105
    days = 5
    portions_per_day = total_portions / days
    puppies_per_portion = total_puppies / portions_per_day
    result = puppies_per_portion
    return result

print(solution())