def solution():
    """John has 20% more boxes than Jules. Jules has 5 more boxes than Joseph. Joseph has 80% fewer boxes than Stan. If Stan has 100 boxes, how many boxes does John have?"""
    # Define the number of boxes Stan has
    stan_boxes = 100

    # Calculate the number of boxes Joseph has
    joseph_boxes = stan_boxes * 0.2 * 0.2 * 0.2

    # Calculate the number of boxes Jules has
    jules_boxes = joseph_boxes + 5

    # Calculate the number of boxes John has
    john_boxes = jules_boxes * 1.2

    # return the result
    result = john_boxes
    return result

print(solution())