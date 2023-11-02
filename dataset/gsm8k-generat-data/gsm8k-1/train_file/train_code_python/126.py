def solution():
    """Three cats sat on a fence, meowing at the moon. The first cat meowed 3 times per minute. The second cat meowed twice as frequently as the first cat. And the third cat meowed at one-third the frequency of the second cat. What is the combined total number of meows the three cats make in 5 minutes?"""
    cat1_frequency = 3
    cat2_frequency = cat1_frequency * 2
    cat3_frequency = cat2_frequency / 3
    total_meows = (cat1_frequency + cat2_frequency + cat3_frequency) * 5
    result = total_meows
    return result

print(solution())