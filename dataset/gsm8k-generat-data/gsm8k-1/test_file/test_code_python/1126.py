def solution():
    """Nik has 200 crayons. He wants to separate them into groups of 8 and put them into boxes. Each box weighs 8 ounces. Each crayon weighs 1 ounce. If he puts all of his crayons into boxes, what is the total weight, in pounds, of the crayons and the boxes, when there are 16 ounces to a pound?"""
    num_crayons = 200
    crayons_per_box = 8
    num_boxes = num_crayons // crayons_per_box
    weight_per_box = 8  # in ounces
    weight_per_crayon = 1  # in ounces
    total_weight = (num_boxes * weight_per_box) + (num_crayons * weight_per_crayon)
    weight_in_lbs = total_weight / 16
    result = weight_in_lbs
    return result

print(solution())