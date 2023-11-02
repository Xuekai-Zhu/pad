def solution():
    num_boxes = 10
    num_pencils_per_box = None

    # Calculate total number of pencils
    total_pencils = num_boxes * num_pencils_per_box + 10

    # Calculate number of pencils shared with friends
    shared_pencils = total_pencils - 10

    # Calculate number of pencils each friend received
    num_friends = 5
    num_pencils_per_friend = 8
    total_pencils_shared = num_friends * num_pencils_per_friend

    # Calculate number of pencils in each box
    num_pencils_per_box = (shared_pencils - total_pencils_shared) / num_boxes
    result = num_pencils_per_box
    return result

print(solution())