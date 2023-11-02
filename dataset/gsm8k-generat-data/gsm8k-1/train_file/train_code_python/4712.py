def solution():
    """Ali and Sara ate 80 small apples combined. Ali ate 4 times more apples than Sara. How many apples did Sara eat?"""
    total_apples = 80
    ratio_sara_to_ali = 1 / 4
    sara_apples = total_apples / (1 + ratio_sara_to_ali)
    result = sara_apples
    return result

print(solution())