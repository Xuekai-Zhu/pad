def solution():
    """There were 180 apples in each crate. 12 such crates of apples were delivered to a factory. 160 apples were rotten and had to be thrown away. The remaining apples were packed into boxes of 20 apples each. How many boxes of apples were there?"""
    # Define the number of apples per crate
    APPLES_PER_CRATE = 180

    # Define the number of crates delivered
    crates_delivered = 12

    # Calculate the total number of apples delivered
    total_apples = APPLES_PER_CRATE * crates_delivered

    # Subtract the number of rotten apples
    total_apples -= 160

    # Calculate the number of boxes of apples
    boxes = total_apples // 20

    # Display the number of boxes
    result = boxes
    return result

print(solution())