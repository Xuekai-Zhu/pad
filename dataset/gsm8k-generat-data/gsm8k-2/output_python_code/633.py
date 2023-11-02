def solution():
    """Vaishali has 4 hats, each with three stripes. She also has three hats with four stripes each, six hats with no stripes, and another two hats with 5 stripes each. What is the combined total number of stripes Vaishali has on all of her hats?"""
    hats_with_3_stripes = 4
    hats_with_4_stripes = 3
    hats_with_no_stripes = 6
    hats_with_5_stripes = 2
    total_stripes = (hats_with_3_stripes*3) + (hats_with_4_stripes*4) + (hats_with_5_stripes*5)
    result = total_stripes
    return result

print(solution())