def solution():
    """ Lena has 16 candy bars. She needs 5 more candy bars to have 3 times as many as Kevin, and Kevin has 4 candy bars less than Nicole. How many more candy bars does Lena have than Nicole? """
    # Define Lena's candy bars
    lena_candy = 16

    # Determine Kevin's candy bars
    kevin_candy = (lena_candy + 5) / 3

    # Determine Nicole's candy bars
    nicole_candy = kevin_candy + 4

    # Calculate the difference between Lena's and Nicole's candy bars
    diff = lena_candy - nicole_candy

    # return the result
    result = diff
    return result

print(solution())