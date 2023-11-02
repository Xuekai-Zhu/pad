def solution():
    """For a project, a builder purchased 7 boxes of bolts with each box containing 11 bolts. He purchased 3 boxes of nuts with each box containing 15 nuts. He ended up finishing the project 6 days early and with 3 bolts and 6 nuts left over. How many bolts and nuts did he use for the project?"""
    bolts_per_box = 11
    nuts_per_box = 15
    num_boxes_bolts = 7
    num_boxes_nuts = 3
    bolts_leftover = 3
    nuts_leftover = 6
    total_bolts = bolts_per_box * num_boxes_bolts - bolts_leftover
    total_nuts = nuts_per_box * num_boxes_nuts - nuts_leftover
    result = f"The builder used {total_bolts} bolts and {total_nuts} nuts for the project."
    return result

print(solution())