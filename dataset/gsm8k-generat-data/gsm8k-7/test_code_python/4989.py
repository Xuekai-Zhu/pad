def solution():
    wrapper_per_box = 18
    wrapper_per_day = 90
    days = 3

    # Calculate the total amount of wrapper Edmund has in 3 days
    total_wrapper = wrapper_per_day * days

    # Calculate the number of gift boxes Edmund can wrap
    num_boxes = total_wrapper // wrapper_per_box

    result = num_boxes
    return result

print(solution())