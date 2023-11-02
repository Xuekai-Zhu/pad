def solution():
    rose_shampoo = 1/3  # Janet has 1/3 of a bottle of rose shampoo
    jasmine_shampoo = 1/4  # Janet has 1/4 of a bottle of jasmine shampoo
    shampoo_per_day = 1/12  # Janet uses 1/12 of a bottle of shampoo per day

    # Calculate the total amount of shampoo
    total_shampoo = rose_shampoo + jasmine_shampoo

    # Calculate the number of days the shampoo will last
    days_last = total_shampoo / shampoo_per_day

    result = days_last
    return result

print(solution())