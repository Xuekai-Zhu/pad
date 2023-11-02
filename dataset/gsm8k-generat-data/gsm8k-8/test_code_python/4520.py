def solution():
    # Let's assume Cyrus has x colored pencils
    x = 1
    # Cheryl has thrice as many as Cyrus
    cheryl = 3 * x
    # Madeline has half of what Cheryl has
    madeline = 0.5 * cheryl

    # The total number of colored pencils is the sum of all three
    total = cheryl + madeline + 63
    result = total
    return result

print(solution())