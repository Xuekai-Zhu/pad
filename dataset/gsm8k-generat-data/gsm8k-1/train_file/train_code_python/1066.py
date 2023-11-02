def solution():
    """There were 180 apples in each crate. 12 such crates of apples were delivered to a factory. 
    160 apples were rotten and had to be thrown away. The remaining apples were packed into boxes of 20 apples each. 
    How many boxes of apples were there?"""
    apples_per_crate = 180
    total_crates = 12
    rotten_apples = 160
    usable_apples = (apples_per_crate * total_crates) - rotten_apples
    boxes = usable_apples / 20
    result = boxes
    
    return result

print(solution())