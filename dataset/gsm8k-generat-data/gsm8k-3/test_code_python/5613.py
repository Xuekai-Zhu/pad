def solution():
    """Pete's memory card can hold 3,000 pictures of 8 megabytes each. How many pictures can it hold of 6 megabytes each?"""
    # Define the size of each picture in megabytes
    PICTURE_SIZE_8MB = 8
    PICTURE_SIZE_6MB = 6

    # Define the maximum number of pictures the memory card can hold
    MAX_PICTURES = 3000

    # Calculate the number of pictures the memory card can hold of 6MB each
    pictures_6mb = (PICTURE_SIZE_8MB / PICTURE_SIZE_6MB) * MAX_PICTURES

    # Display the result
    result = int(pictures_6mb)
    return result

print(solution())