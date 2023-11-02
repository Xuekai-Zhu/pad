def solution():
    """There are 42 apples in a crate. 12 crates of apples were delivered to a factory. 4 apples were rotten and had to be thrown away. The remaining apples were packed into boxes that could fit 10 apples each. How many boxes of apples were there?"""
    # Define the number of apples in a crate and the number of crates delivered
    APPLES_PER_CRATE = 42
    CRATES_DELIVERED = 12

    # Calculate the total number of apples delivered
    total_apples = APPLES_PER_CRATE * CRATES_DELIVERED

    # Subtract the number of rotten apples
    total_apples -= 4

    # Calculate the number of boxes needed to pack the remaining apples
    boxes_needed = total_apples // 10

    # Display the number of boxes needed
    result = boxes_needed
    return result

print(solution())