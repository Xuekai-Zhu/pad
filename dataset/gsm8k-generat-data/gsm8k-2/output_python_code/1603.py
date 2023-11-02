def solution():
    """Mary and Mike are sharing a jar of paint. Mary paints a dragon using 3 square feet worth of paint. Mike paints a castle using 2 square feet more paint than Mary used on her dragon.
    They both then work together to paint the biggest sun possible. If there was originally enough paint in the jar to cover 13 square feet, how many square feet of paint can be used to paint the sun?"""
    mary_paint = 3
    mike_paint = mary_paint + 2
    total_paint_used = mary_paint + mike_paint
    remaining_paint = 13 - total_paint_used
    result = remaining_paint
    return result

print(solution())