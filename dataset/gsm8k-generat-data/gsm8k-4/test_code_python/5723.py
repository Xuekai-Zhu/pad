def solution():
    """There are 160 tissues inside a tissue box. If Tucker bought 3 boxes, and used 210 tissues while he was sick with the flu, how many tissues would he have left?"""
    # Define the number of tissues per box
    tissues_per_box = 160

    # Calculate the total number of tissues Tucker bought
    total_tissues = tissues_per_box * 3

    # Calculate the number of tissues he has left after using some
    tissues_left = total_tissues - 210

    result = tissues_left
    return result

print(solution())