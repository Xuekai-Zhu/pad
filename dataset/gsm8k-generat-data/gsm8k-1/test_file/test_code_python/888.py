def solution():
    """Ellen is on a diet. She eats two carrots, a salad, and a yogurt every day. The salad costs her $6, while the yogurt is half the price. How much does Ellen pay for one carrot every day when in total she pays $11 for her goods?"""
    salad_cost = 6
    yogurt_cost = salad_cost / 2
    carrot_cost = (11 - salad_cost - yogurt_cost) / 2
    result = carrot_cost
    return result

print(solution())