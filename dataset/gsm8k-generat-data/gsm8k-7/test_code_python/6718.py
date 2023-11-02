def solution():
    rose_shampoo = 1/3
    jasmine_shampoo = 1/4
    shampoo_per_day = 1/12

    # Calculate the total amount of shampoo in bottles
    total_shampoo = rose_shampoo + jasmine_shampoo

    # Calculate the total amount of shampoo in days
    total_days = total_shampoo / shampoo_per_day
    result = total_days
    return result

print(solution())