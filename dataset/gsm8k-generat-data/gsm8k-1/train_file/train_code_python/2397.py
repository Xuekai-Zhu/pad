def solution():
    """A piece of wire 5 feet 4 inches long was divided into 4 equal parts. How long was each part in inches if 1 foot is equal to 12 inches?"""
    total_length_inches = 5*12 + 4
    parts = 4
    length_per_part_inches = total_length_inches / parts
    result = length_per_part_inches
    return result

print(solution())