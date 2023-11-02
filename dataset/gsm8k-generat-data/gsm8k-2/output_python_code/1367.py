def solution():
    """Tamara is 3 times Kim's height less 4 inches. Tamara and Kim have a combined height of 92 inches. How many inches tall is Tamara?"""
    combined_height = 92
    tamara_height = (3 * kim_height) - 4
    kim_height = (combined_height + 4) / 4
    tamara_height = 3 * kim_height - 4
    result = tamara_height
    return result

print(solution())