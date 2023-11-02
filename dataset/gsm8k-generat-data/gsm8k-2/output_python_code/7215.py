def solution():
    """James was 2/3s as tall as his uncle who is 72 inches. He gets a growth spurt that makes him gain 10 inches. How much taller is his uncle than James now?"""
    uncle_height = 72
    james_height = (2/3) * uncle_height
    james_height += 10
    height_difference = uncle_height - james_height
    result = height_difference
    return result

print(solution())