def solution():
    """A bakery produces 60 loaves of bread each day. Two-thirds of the loaves are sold in the morning and half of what is left is sold equally in the afternoon and evening. How many loaves of bread are sold in the afternoon?"""
    total_bread = 60
    morning_bread = total_bread * (2/3)
    leftover_bread = total_bread - morning_bread
    afternoon_bread = leftover_bread / 2
    result = afternoon_bread
    return result

print(solution())