def solution():
    """Lewis found 4 more items on the scavenger hunt than Samantha. Samantha found four times the amount of items than Tanya who was only able to find 4 items. How many items did Lewis find?"""
    # Define the number of items Tanya found
    tanya_items = 4

    # Calculate the number of items Samantha found
    samantha_items = tanya_items * 4

    # Calculate the number of items Lewis found
    lewis_items = samantha_items + 4

    # return the result
    result = lewis_items
    return result

print(solution())