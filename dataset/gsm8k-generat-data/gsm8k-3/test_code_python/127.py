def solution():
    """Three cats sat on a fence, meowing at the moon.  The first cat meowed 3 times per minute.  The second cat meowed twice as frequently as the first cat.  And the third cat meowed at one-third the frequency of the second cat.  What is the combined total number of meows the three cats make in 5 minutes?"""
    # Define the meow frequency of each cat
    cat1_freq = 3
    cat2_freq = cat1_freq * 2
    cat3_freq = cat2_freq / 3

    # Calculate the total number of meows each cat makes in 5 minutes
    cat1_meows = cat1_freq * 5
    cat2_meows = cat2_freq * 5
    cat3_meows = cat3_freq * 5

    # Calculate the combined total number of meows
    total_meows = cat1_meows + cat2_meows + cat3_meows

    # return the result
    result = total_meows
    return result

print(solution())