def solution():
    """Every hour, Paige can bake 2 banana bread loaves in the oven. Each banana bread loaf is cut into 8 slices and wrapped individually for sale. Each slice is sold for 50 cents for a fundraiser. If she baked from 1:00 PM - 6:00 PM straight, and sold all the slices, how much did she raise in dollars?"""
    loaves_per_hour = 2
    slices_per_loaf = 8
    slices_per_hour = loaves_per_hour * slices_per_loaf
    hours_baked = 5
    total_slices = slices_per_hour * hours_baked
    price_per_slice = 0.5
    total_money = total_slices * price_per_slice
    result = total_money
    return result

print(solution())