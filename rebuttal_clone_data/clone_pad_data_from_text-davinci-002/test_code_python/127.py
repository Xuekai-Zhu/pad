def solution():
    """Three cats sat on a fence, meowing at the moon. The first cat meowed 3 times per minute. The second cat meowed twice as frequently as the first cat. And the third cat meowed at one-third the frequency of the second cat. What is the combined total number of meows the three cats make in 5 minutes?"""
    cat1_meows_per_minute = 3
    cat2_meows_per_minute = cat1_meows_per_minute * 2
    cat3_meows_per_minute = cat2_meows_per_minute / 3
    total_meows_per_minute = cat1_meows_per_minute + cat2_meows_per_minute + cat3_meows_per_minute
    minutes = 5
    total_meows = total_meows_per_minute * minutes
    result = total_meows
    return result

print(solution())