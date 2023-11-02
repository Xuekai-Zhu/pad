def solution():
    """Lewis found 4 more items on the scavenger hunt than Samantha. Samantha found four times the amount of items than Tanya who was only able to find 4 items. How many items did Lewis find?"""
    tanya_items = 4
    samantha_items = tanya_items * 4
    lewis_items = samantha_items + 4
    result = lewis_items
    return result

print(solution())