def solution():
    """A crayon factory makes 4 colors of crayons. They put 2 of each color crayon in each box. The factory produces enough crayons to fill 5 boxes per hour. How many crayons does the factory produce in 4 hours?"""
    colors_of_crayons = 4
    crayons_per_color = 2
    boxes_per_hour = 5
    hours = 4
    total_boxes = boxes_per_hour * hours
    total_crayons = total_boxes * colors_of_crayons * crayons_per_color
    result = total_crayons
    return result

print(solution())