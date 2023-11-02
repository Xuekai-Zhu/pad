def solution():
    """Arnel had ten boxes of pencils with the same number of pencils in each box. He kept ten pencils and shared the remaining pencils equally with his five friends. If his friends got eight pencils each, how many pencils are in each box?"""
    # Define the number of boxes and remaining pencils after Arnel kept ten
    num_boxes = 10
    remaining_pencils = num_boxes * (x-10)

    # Determine the number of pencils in each box
    pencils_per_box = remaining_pencils / (5 * 8)

    result = pencils_per_box
    return result

print(solution())