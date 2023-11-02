def solution():
    """Arnel had ten boxes of pencils with the same number of pencils in each box. He kept ten pencils and shared the remaining pencils equally with his five friends. If his friends got eight pencils each, how many pencils are in each box?"""
    # Define the total number of boxes and the number of pencils Arnel kept
    num_boxes = 10
    num_pencils_kept = 10

    # Calculate the total number of pencils and the number of pencils shared with friends
    total_pencils = num_boxes * (10 + num_pencils_kept)
    pencils_shared = total_pencils - num_pencils_kept

    # Calculate the number of pencils in each box
    pencils_per_box = pencils_shared / (num_boxes - 1)

    # return the result
    result = pencils_per_box
    return result

print(solution())