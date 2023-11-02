def solution():
    """Daniel buys a magazine costing $0.85 and a pencil costing $0.50. He pays with a coupon that gives him $0.35 off. How much does he spend?"""
    magazine_cost = 0.85
    pencil_cost = 0.50
    coupon_amount = 0.35
    total_cost = magazine_cost + pencil_cost - coupon_amount
    result = total_cost
    return result

print(solution())