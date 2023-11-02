def solution():
    """Hooper Bay has twice as many pounds of lobster than the two other harbors combined. If the other two harbors have 80 pounds of lobster each, how many pounds of lobster are the three harbors holding?"""
    harbor1 = 80
    harbor2 = 80
    hooper_bay = harbor1 + harbor2 * 2
    total_lobster = harbor1 + harbor2 + hooper_bay
    result = total_lobster
    return result

print(solution())