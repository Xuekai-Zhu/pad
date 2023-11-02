def solution():
    
    hats_with_three_stripes = 4
    hats_with_four_stripes = 3
    hats_with_no_stripes = 6
    hats_with_five_stripes = 2
    total_stripes_on_hats = (hats_with_three_stripes * 3) + (hats_with_four_stripes * 4) + (hats_with_no_stripes * 0) + (hats_with_five_stripes * 5)
    result = total_stripes_on_hats
    return result

print(solution())