def solution():
    """All 20 of Grant’s baby teeth have fallen out and he has a total of $54 from the tooth fairy. Every time he lost a tooth, he put it under his pillow for the tooth fairy, except for one that he dropped on the way home from school and another he swallowed accidentally. The tooth fairy left Grant $20 when he lost his first tooth. How much did the tooth fairy leave him per tooth after his first tooth, assuming equal money exchanged for each tooth thereafter?"""
    total_teeth = 20
    lost_teeth = 18
    total_money = 54
    first_tooth_money = 20
    remaining_money = total_money - first_tooth_money
    money_per_tooth = remaining_money / lost_teeth
    result = money_per_tooth
    return result

print(solution())