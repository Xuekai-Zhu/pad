def solution():
    stan_boxes = 100

    # Calculate Joseph's boxes
    joseph_boxes = stan_boxes * 0.2 * 0.2 * 100

    # Calculate Jules' boxes
    jules_boxes = joseph_boxes + 5

    # Calculate John's boxes
    john_boxes = jules_boxes * 1.2

    result = john_boxes
    return result

print(solution())