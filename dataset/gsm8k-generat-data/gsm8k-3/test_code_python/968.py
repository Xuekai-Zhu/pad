def solution():
    """Mary has 26 blue shirts and 36 brown shirts. If she gives away half of her blue shirts and a third of her brown shirts, how many shirts does she have left?"""
    # Define the initial number of blue and brown shirts
    blue_shirts = 26
    brown_shirts = 36

    # Calculate the new number of blue and brown shirts after giving away half and one third, respectively
    blue_shirts = blue_shirts // 2
    brown_shirts = brown_shirts // 3

    # Calculate the total number of shirts Mary has left
    total_shirts = blue_shirts + brown_shirts

    # Display the total number of shirts Mary has left
    result = total_shirts
    return result

print(solution())