def solution():
    """All 20 of Grant’s baby teeth have fallen out and he has a total of $54 from the tooth fairy. Every time he lost a tooth, he put it under his pillow for the tooth fairy, except for one that he dropped on the way home from school and another he swallowed accidentally. The tooth fairy left Grant $20 when he lost his first tooth. How much did the tooth fairy leave him per tooth after his first tooth, assuming equal money exchanged for each tooth thereafter?"""
    total_teeth = 20
    money_total = 54
    money_first_tooth = 20
    teeth_lost = total_teeth - 2
    money_lost = money_total - money_first_tooth
    money_per_tooth = money_lost / teeth_lost
    result = round(money_per_tooth, 2)
    return result

print(solution())