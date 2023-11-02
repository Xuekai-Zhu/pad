def solution():
    """A pen costs as much as a pencil and eraser combined. A pencil costs $1.20 and an eraser costs $0.30. How much will 8 pens cost?"""
    pencil_cost = 1.20
    eraser_cost = 0.30
    pen_cost = pencil_cost + eraser_cost
    pens_needed = 8
    total_cost = pen_cost * pens_needed
    result = total_cost
    return result

print(solution())