def solution():
    """Three cats sat on a fence, meowing at the moon. The first cat meowed 3 times per minute. The second cat meowed twice as frequently as the first cat. And the third cat meowed at one-third the frequency of the second cat. What is the combined total number of meows the three cats make in 5 minutes?"""
    # Define the meowing frequency of each cat
    cat1_freq = 3
    cat2_freq = 2 * cat1_freq
    cat3_freq = cat2_freq / 3

    # Calculate the total number of meows in 5 minutes
    total_meows = 5 * (cat1_freq + cat2_freq + cat3_freq)

    # Return the result
    result = total_meows
    return result

print(solution())