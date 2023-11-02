def solution():
    """If Brooke adds eight balloons to his current 12, and Tracy adds 24 to her current 6, how many balloons will they have in total if Tracy pops half of her balloons?"""
    brooke_balloons = 12 + 8
    tracy_balloons = 6 + 24
    tracy_balloons = tracy_balloons / 2
    total_balloons = brooke_balloons + tracy_balloons
    result = total_balloons
    return result

print(solution())