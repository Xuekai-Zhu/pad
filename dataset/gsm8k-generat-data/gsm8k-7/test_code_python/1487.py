def solution():
    initial_hens = 10
    initial_eggs = 80
    initial_days = 10

    new_hens = 15
    new_total_hens = initial_hens + new_hens

    new_days = 15

    # Calculate the average number of eggs laid per hen in 10 days
    avg_eggs_per_hen = initial_eggs / initial_hens

    # Calculate the total number of eggs laid by all hens in 10 days
    total_eggs_initial = initial_hens * avg_eggs_per_hen

    # Calculate the average number of eggs laid per hen in 15 days
    avg_eggs_per_hen_new = avg_eggs_per_hen * (new_days / initial_days)

    # Calculate the total number of eggs laid by all hens in 15 days
    total_eggs_new = new_total_hens * avg_eggs_per_hen_new

    # Calculate the total number of eggs laid by all hens in 15 days (rounded to the nearest whole number)
    total_eggs_new_rounded = round(total_eggs_new)
    result = total_eggs_new_rounded
    return result

print(solution())