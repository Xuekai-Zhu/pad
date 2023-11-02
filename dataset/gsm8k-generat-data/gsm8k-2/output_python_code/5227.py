def solution():
    """There are 42 apples in a crate. 12 crates of apples were delivered to a factory. 4 apples were rotten and had to be thrown away. The remaining apples were packed into boxes that could fit 10 apples each. How many boxes of apples were there?"""
    apples_per_crate = 42
    num_crates = 12
    num_rotten_apples = 4
    total_apples = apples_per_crate * num_crates - num_rotten_apples
    num_boxes = total_apples // 10
    result = num_boxes
    return result

print(solution())