def solution():
    """Matt can paint a house in 12 hours. Patty can paint the same house in one third the time. Rachel can paint the same house in 5 more than double the amount of hours as Patty. How long will it take Rachel to paint the house?"""
    matt_hours = 12
    patty_hours = matt_hours / 3
    rachel_hours = (2 * patty_hours) + 5
    result = rachel_hours
    return result

print(solution())