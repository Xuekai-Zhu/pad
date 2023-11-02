def solution():
    """Vlad is 6 feet, 3 inches tall. His younger sister is 2 feet, 10 inches tall. How many inches taller is Vlad than his sister?"""
    vlad_height_inches = (6 * 12) + 3
    sister_height_inches = (2 * 12) + 10
    height_difference_inches = vlad_height_inches - sister_height_inches
    result = height_difference_inches
    return result

print(solution())