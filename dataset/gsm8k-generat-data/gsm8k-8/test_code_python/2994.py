def solution():
    hose_off_time = 10
    shampoo_time = 15
    num_shampoos = 3

    total_shampoo_time = shampoo_time * num_shampoos
    total_time = hose_off_time + total_shampoo_time
    result = total_time
    return result

print(solution())