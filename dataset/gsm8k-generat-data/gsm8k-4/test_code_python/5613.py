def solution():
    """Pete's memory card can hold 3,000 pictures of 8 megabytes each. How many pictures can it hold of 6 megabytes each?"""
    # Define the capacity of the memory card in megabytes and the size of each picture
    CARD_CAPACITY = 3000 * 8
    PICTURE_SIZE = 6

    # Calculate the number of pictures the memory card can hold of 6 megabytes each
    pictures_6mb = CARD_CAPACITY // (PICTURE_SIZE * 1024)

    # return the result
    result = pictures_6mb
    return result

print(solution())