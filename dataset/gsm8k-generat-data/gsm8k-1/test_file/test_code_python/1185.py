def solution():
    """Doxa sliced an apple into 8 pieces. She ate 1 slice, her sister ate 1 more than her, and her brother ate 1 more than her sister. How many slices of apple did they all eat?"""
    doxa_slices = 1
    sister_slices = doxa_slices + 1
    brother_slices = sister_slices + 1
    total_slices = doxa_slices + sister_slices + brother_slices
    result = total_slices
    return result

print(solution())