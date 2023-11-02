def solution():
    # Calculate the number of boxes Joseph has
    stan_boxes = 100
    joseph_boxes = stan_boxes * 0.2

    # Calculate the number of boxes Jules has
    jules_boxes = joseph_boxes + 5

    # Calculate the number of boxes John has
    john_boxes = jules_boxes * 1.2

    result = john_boxes
    return result

print(solution())