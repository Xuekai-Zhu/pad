def solution():
    """John has 3 boxes. Each box is 5 inches by 6 inches by 4 inches. The walls are 1 inch thick. What is the total inner volume of all 3 boxes?"""
    box_length = 5
    box_width = 6
    box_height = 4
    wall_thickness = 1
    inner_length = box_length - 2 * wall_thickness
    inner_width = box_width - 2 * wall_thickness
    inner_height = box_height - 2 * wall_thickness
    inner_volume = inner_length * inner_width * inner_height
    total_inner_volume = inner_volume * 3
    result = total_inner_volume
    return result

print(solution())