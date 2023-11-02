def solution():
    """Three cats sat on a fence, meowing at the moon. The first cat meowed 3 times per minute. The second cat meowed twice as frequently as the first cat. And the third cat meowed at one-third the frequency of the second cat. What is the combined total number of meows the three cats make in 5 minutes?"""
    first_cat_rate = 3
    second_cat_rate = 2 * first_cat_rate
    third_cat_rate = second_cat_rate / 3
    total_meows = (first_cat_rate + second_cat_rate + third_cat_rate) * 5
    result = total_meows
    return result

print(solution())