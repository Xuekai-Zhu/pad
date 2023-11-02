def solution():
    stan_boxes = 100  # Stan has 100 boxes
    joseph_boxes = stan_boxes * 0.2  # Joseph has 80% fewer boxes than Stan
    jules_boxes = joseph_boxes + 5  # Jules has 5 more boxes than Joseph
    john_boxes = jules_boxes * 1.2  # John has 20% more boxes than Jules

    result = john_boxes
    return result

print(solution())