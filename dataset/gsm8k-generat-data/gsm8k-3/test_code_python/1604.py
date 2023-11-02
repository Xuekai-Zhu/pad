def solution():
    """Mary and Mike are sharing a jar of paint. Mary paints a dragon using 3 square feet worth of paint. Mike paints a castle using 2 square feet more paint than Mary used on her dragon. They both then work together to paint the biggest sun possible. If there was originally enough paint in the jar to cover 13 square feet, how many square feet of paint can be used to paint the sun?"""
    # Define the amount of paint used for the dragon and castle
    dragon_paint = 3
    castle_paint = dragon_paint + 2

    # Calculate the total amount of paint used by Mary and Mike
    total_paint = dragon_paint + castle_paint

    # Calculate the remaining amount of paint in the jar after the dragon and castle are painted
    remaining_paint = 13 - total_paint

    # The sun requires the remaining paint, so the total square feet of paint that can be used for the sun is the remaining paint
    result = remaining_paint
    return result

print(solution())