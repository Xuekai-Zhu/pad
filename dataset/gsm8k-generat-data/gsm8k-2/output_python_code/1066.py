def solution():
    """There were 180 apples in each crate. 12 such crates of apples were delivered to a factory. 160 apples were rotten and had to be thrown away. The remaining apples were packed into boxes of 20 apples each. How many boxes of apples were there?"""
    apples_per_crate = 180
    num_crates = 12
    num_rotten = 160
    num_good_apples = (apples_per_crate * num_crates) - num_rotten
    num_boxes = num_good_apples // 20
    result = num_boxes
    return result

print(solution())