def solution():
    """
    Parker wants to find out what the average percentage of kernels that pop in a bag is.
    In the first bag he makes, 60 kernels pop and the bag has 75 kernels.
    In the second bag, 42 kernels pop and there are 50 in the bag.
    In the final bag, 82 kernels pop and the bag has 100 kernels.
    """
    # Calculate the percentage of kernels that popped in each bag
    percent_1 = (60/75) * 100
    percent_2 = (42/50) * 100
    percent_3 = (82/100) * 100

    # Calculate the average percentage of kernels that popped
    average_percent = (percent_1 + percent_2 + percent_3) / 3

    # Display the average percentage of kernels that popped
    result = average_percent
    return result

print(solution())