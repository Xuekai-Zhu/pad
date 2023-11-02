def solution():
    """Jen and Tyler are gymnasts practicing flips. Jen is practicing the triple-flip while Tyler is practicing the double-flip. Jen did sixteen triple-flips during practice. Tyler flipped in the air half the number of times Jen did. How many double-flips did Tyler do?"""
    jen_flips = 16 * 3
    tyler_flips = jen_flips / 2
    double_flips = tyler_flips / 2
    result = double_flips
    return result

print(solution())