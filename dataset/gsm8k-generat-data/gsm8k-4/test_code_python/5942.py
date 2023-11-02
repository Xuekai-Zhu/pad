def solution():
    """Tyrah has six times as many pencils as Sarah has. Tim has eight times as many pencils as Sarah. If Tyrah has 12 pencils, how many does Tim have?"""
    # Determine how many pencils Sarah has
    sarah_pencils = 12 / 6

    # Determine how many pencils Tim has
    tim_pencils = sarah_pencils * 8

    result = tim_pencils
    return result

print(solution())