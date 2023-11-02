def solution():
    gabriel_grandkids = 6

    # Let x be the number of children Yasmin has
    # Then John has 2*x children
    total_children = x + 2*x

    # The total number of children is also the number of grandkids Gabriel has
    # So we can solve for x using the equation: gabriel_grandkids = total_children
    x = gabriel_grandkids / 3

    result = x  # Yasmin's number of children
    return result

print(solution())