def solution():
    admission_price = 30
    kids_price = admission_price / 2
    soda_price = 5
    group_size = 10
    num_children = 4
    total_price = (admission_price * group_size) - ((admission_price * group_size) * 0.2) + (soda_price)
    result = total_price
    return result

print(solution())