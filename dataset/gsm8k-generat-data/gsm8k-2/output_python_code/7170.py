def solution():
    """A crayon factory makes 4 colors of crayons. They put 2 of each color crayon in each box. The factory produces enough crayons to fill 5 boxes per hour. How many crayons does the factory produce in 4 hours?"""
    num_colors = 4
    num_crayons_per_color = 2
    num_crayons_per_box = num_colors * num_crayons_per_color
    num_boxes_per_hour = 5
    num_crayons_per_hour = num_boxes_per_hour * num_crayons_per_box
    total_crayons = num_crayons_per_hour * 4
    result = total_crayons
    return result

print(solution())