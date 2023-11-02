def solution():
    """Jen and Tyler are gymnasts practicing flips. Jen is practicing the triple-flip while Tyler is practicing the double-flip. Jen did sixteen triple-flips during practice. Tyler flipped in the air half the number of times Jen did. How many double-flips did Tyler do?"""
    # Define the number of triple flips Jen did
    jen_flips = 16

    # Calculate the number of flips Tyler did
    tyler_flips = jen_flips / 2

    # Calculate the number of double flips Tyler did
    tyler_double_flips = tyler_flips / 2

    # Round the result to the nearest integer
    result = round(tyler_double_flips)
    return result

print(solution())