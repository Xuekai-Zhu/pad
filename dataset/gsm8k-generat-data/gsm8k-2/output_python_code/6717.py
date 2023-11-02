def solution():
    """Janet has 1/3 of a bottle of rose shampoo and 1/4 of a bottle of jasmine shampoo. If she uses 1/12 of a bottle of shampoo per day, how many days will her shampoo last?"""
    rose_shampoo = 1/3
    jasmine_shampoo = 1/4
    total_shampoo = rose_shampoo + jasmine_shampoo
    shampoo_per_day = 1/12
    days_of_use = total_shampoo / shampoo_per_day
    result = days_of_use
    return result

print(solution())