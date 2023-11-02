def solution():
    """Mark wants to build a pyramid of soda cases that's four levels tall. Each level of the pyramid has a square base where each side is one case longer than the level above it. The top level is just one case. How many cases of soda does Mark need?"""
    height = 4
    total_cases = 0
    for i in range(height):
        length = i + 1
        total_cases += length ** 2
    result = total_cases
    return result

print(solution())