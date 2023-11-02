def solution():
    # Let's assume Cyrus has x colored pencils
    # Then Cheryl has 3x colored pencils
    # And Madeline has (1/2)*(3x) = (3/2)x colored pencils
    # We know Madeline has 63 colored pencils, so (3/2)x = 63
    x = 42  # Solve for x

    cyrus_pencils = x
    cheryl_pencils = 3 * x
    madeline_pencils = (3/2) * x

    total_pencils = cyrus_pencils + cheryl_pencils + madeline_pencils
    result = total_pencils
    return result

print(solution())