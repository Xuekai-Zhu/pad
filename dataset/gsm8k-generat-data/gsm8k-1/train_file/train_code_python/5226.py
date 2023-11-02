def solution():
    """Julian has 400 legos and wants to make lego models of two identical airplanes. If each airplane model requires 240 legos, how many more legos does Julian need?"""
    total_legos_needed = 2 * 240
    legos_missing = total_legos_needed - 400
    result = legos_missing
    return result

print(solution())