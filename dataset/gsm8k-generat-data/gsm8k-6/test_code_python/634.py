def solution():
    # Calculate total number of stripes Vaishali has on all her hats
    stripes_on_4_hats = 4 * 3
    stripes_on_3_hats = 3 * 4
    stripes_on_2_hats = 2 * 5
    total_stripes = stripes_on_4_hats + stripes_on_3_hats + stripes_on_2_hats
    result = total_stripes
    return result

print(solution())