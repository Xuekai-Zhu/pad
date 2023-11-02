def solution():
    
    trim_up_price = 5
    fancy_shape_price = 15
    num_boxwoods_trimmed = 30
    num_boxwoods_shaped = 4
    total_trim_price = num_boxwoods_trimmed * trim_up_price
    total_fancy_price = num_boxwoods_shaped * fancy_shape_price
    total_price = total_trim_price + total_fancy_price
    result = total_price
    return result

print(solution())