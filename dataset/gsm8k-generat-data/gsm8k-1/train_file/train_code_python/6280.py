def solution():
    """Jenna catches an eel that's 1/3 as long as Bill's. If the combined length of their eels is 64 inches, how long is Jenna's eel?"""
    bill_length = None
    jenna_length = None
    combined_length = 64
    
    # Let x be the length of Jenna's eel in inches
    # Then Bill's eel is 3x inches long
    # The sum of their lengths is 64 inches
    # Therefore, 4x = 64
    # Solving for x, we get:
    jenna_length = 16
    bill_length = 48

    result = jenna_length
    return result

print(solution())