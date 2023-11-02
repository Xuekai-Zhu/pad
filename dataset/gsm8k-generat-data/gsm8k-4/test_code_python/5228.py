def solution():
    """There are 42 apples in a crate. 12 crates of apples were delivered to a factory. 
    4 apples were rotten and had to be thrown away. The remaining apples were packed into boxes that could 
    fit 10 apples each. How many boxes of apples were there?"""
    # Define the number of apples in a crate and the number of crates delivered
    apples_per_crate = 42
    crates_delivered = 12

    # Calculate the total number of apples delivered
    total_apples = apples_per_crate * crates_delivered

    # Subtract the number of rotten apples
    total_apples -= 4

    # Calculate the number of boxes required to pack the remaining apples
    boxes = total_apples // 10

    # return the result
    result = boxes
    return result

print(solution())