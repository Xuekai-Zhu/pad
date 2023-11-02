def solution():
    """Jesse received $50 as a gift to buy what she wants. She goes to the mall and falls in love with a novel that costs her $7. Then she went to lunch because she was very hungry and spent twice as much as the novel cost her. How much money did Jesse have left after going to the mall?"""
    gift_money = 50
    novel_cost = 7
    lunch_cost = 2 * novel_cost
    total_cost = novel_cost + lunch_cost
    money_left = gift_money - total_cost
    result = money_left
    return result

print(solution())