def solution():
    """Mark wants to build a pyramid of soda cases that's four levels tall. Each level of the pyramid has a square base where each side is one case longer than the level above it. The top level is just one case. How many cases of soda does Mark need?"""
    base = 1
    total = 0
    for i in range(4):
        level = base * base
        total += level
        base += 1

    result = total
    return result

print(solution())