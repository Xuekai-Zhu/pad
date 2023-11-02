def solution():
    """Madeline has 5 boxes with 24 crayons in each. She noticed that 5/8 of the crayons in the 2 boxes were not yet used. In the 2 other boxes, only 2/3 of the crayons were used while the last box was not entirely used. How many unused crayons did Madeline have?"""
    box1_unused = (5/8) * 24
    box2_unused = (5/8) * 24
    box3_unused = (2/3) * 24
    box4_unused = (2/3) * 24
    box5_unused = 24 - (5/8) * 24
    total_unused = box1_unused + box2_unused + box3_unused + box4_unused + box5_unused
    result = total_unused
    return result

print(solution())