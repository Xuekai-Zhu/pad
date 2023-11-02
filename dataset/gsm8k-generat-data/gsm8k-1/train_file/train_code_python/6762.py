def solution():
    """John has 20% more boxes than Jules. Jules has 5 more boxes than Joseph. Joseph has 80% fewer boxes than Stan. If Stan has 100 boxes, how many boxes does John have?"""
    stan_boxes = 100
    joseph_boxes = stan_boxes * 0.2
    jules_boxes = joseph_boxes + 5
    john_boxes = jules_boxes * 1.2
    result = john_boxes
    return result

print(solution())