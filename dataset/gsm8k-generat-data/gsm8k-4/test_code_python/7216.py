def solution():
    """James was 2/3s as tall as his uncle who is 72 inches. He gets a growth spurt that makes him gain 10 inches. How much taller is his uncle than James now?"""
    # Calculate James' height before the growth spurt
    james_height = 2/3 * 72

    # Calculate James' height after the growth spurt
    james_height += 10

    # Calculate the height difference between James and his uncle
    height_diff = 72 - james_height

    # Return the result
    result = height_diff
    return result

print(solution())