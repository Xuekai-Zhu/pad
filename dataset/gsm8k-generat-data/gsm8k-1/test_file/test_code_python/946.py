def solution():
    """Bahati, Azibo, and Dinar each contributed to their team's 45 points. Bahati scored the most points and it was 20 more than Azibo scored and 10 more points than Dinar scored. How many points did Azibo score?"""
    total_points = 45
    # Let x be the points scored by Dinar
    x = (total_points - 10) / 3
    # Bahati scored 20 more than Azibo, so let y be Azibo's points
    y = x + 20
    # The sum of all three scores is 45, so we can solve for Bahati's points
    z = total_points - x - y
    azibo_points = y
    result = azibo_points
    return result

print(solution())