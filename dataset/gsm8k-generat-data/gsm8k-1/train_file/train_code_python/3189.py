def solution():
    """Neil charges $5.00 to trim up each boxwood. He charges $15.00 to trim it into a fancy shape. The customer wants the entire 30 boxwood hedge trimmed up. He has also asked for 4 specific boxwoods shaped into spheres. How much will Neil charge?"""
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