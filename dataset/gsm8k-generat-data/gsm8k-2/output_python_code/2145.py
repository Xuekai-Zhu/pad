def solution():
    """Paolo has 14 coconuts, while Dante has thrice as many coconuts as Paolo. If Dante sold 10 of his coconuts,
    how many coconuts did he have left?"""
    paolo_coconuts = 14
    dante_coconuts = 3 * paolo_coconuts
    dante_coconuts -= 10
    result = dante_coconuts
    return result

print(solution())