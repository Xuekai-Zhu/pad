def solution():
    ratio = 1/3  # Jenna's eel is 1/3 as long as Bill's
    total_length = 64  # The combined length of their eels is 64 inches

    # Set up an equation for the lengths of their eels
    # Let x be the length of Bill's eel
    # Jenna's eel is 1/3 as long, so its length is (1/3)x
    # Their lengths add up to 64, so we can write:
    # x + (1/3)x = 64
    # Solving for x, we get:
    # (4/3)x = 64
    # x = (3/4) * 64
    # x = 48
    # So Bill's eel is 48 inches long, and Jenna's eel is 1/3 of that, or:
    jenna_length = ratio * 48
    result = jenna_length
    return result

print(solution())