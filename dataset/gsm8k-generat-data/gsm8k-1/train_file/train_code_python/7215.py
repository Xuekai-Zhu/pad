def solution():
    """James was 2/3s as tall as his uncle who is 72 inches. He gets a growth spurt that makes him gain 10 inches. How much taller is his uncle than James now?"""
    uncle_height = 72
    james_height = (2/3) * uncle_height
    new_james_height = james_height + 10
    diff_height = uncle_height - new_james_height
    result = diff_height
    return result

print(solution())