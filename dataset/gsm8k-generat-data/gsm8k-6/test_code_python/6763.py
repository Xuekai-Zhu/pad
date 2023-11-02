def solution():
    # Calculate the number of boxes each person has
    stan_boxes = 100
    joseph_boxes = stan_boxes * 0.2 / 0.8  # Joseph has 80% fewer boxes than Stan
    jules_boxes = joseph_boxes + 5  # Jules has 5 more boxes than Joseph
    john_boxes = jules_boxes * 1.2  # John has 20% more boxes than Jules

    result = john_boxes
    return result

print(solution())