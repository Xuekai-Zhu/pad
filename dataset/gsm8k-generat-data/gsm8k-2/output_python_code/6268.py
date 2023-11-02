def solution():
    """Tommy has 13 items in his pencil case. The pens are twice as many as the pencils and there's one eraser. How many pencils are there?"""
    total_items = 13
    eraser = 1
    pens = (total_items - eraser) / 3 * 2
    pencils = (total_items - eraser - pens)
    result = pencils
    return result

print(solution())