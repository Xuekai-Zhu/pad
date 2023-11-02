def solution():
    """There were 180 apples in each crate. 12 such crates of apples were delivered to a factory. 160 apples were rotten and had to be thrown away. The remaining apples were packed into boxes of 20 apples each. How many boxes of apples were there?"""
    # Define the number of apples per crate
    APPLES_PER_CRATE = 180

    # Calculate the total number of apples
    total_apples = APPLES_PER_CRATE * 12

    # Subtract the number of rotten apples
    good_apples = total_apples - 160

    # Calculate the number of boxes of apples
    boxes = good_apples // 20

    result = boxes
    return result

print(solution())