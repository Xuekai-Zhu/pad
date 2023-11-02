def solution():
    # Calculate the total number of pencils before sharing
    total_pencils = 10 * x + 10

    # Calculate the number of pencils shared equally among the friends
    shared_pencils = total_pencils - 10

    # Calculate the number of pencils each friend received
    friend_pencils = 8
    num_friends = 5
    total_friend_pencils = friend_pencils * num_friends

    # Calculate the total number of pencils at the start
    start_total = total_friend_pencils + shared_pencils

    # Calculate the number of pencils in each box
    num_boxes = 10
    pencils_per_box = start_total // num_boxes

    result = pencils_per_box
    return result

print(solution())