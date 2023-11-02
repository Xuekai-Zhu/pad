def solution():
    """Tim decides to light off some fireworks for the fourth of July. He buys a package of fireworks worth $400 and another pack worth twice that much. He gets a 20% discount on them. He also buys a finale firework that costs $150. How much did he spend in total?"""
    package1_cost = 400
    package2_cost = 2 * package1_cost
    discount_percent = 20
    discount_amount = (discount_percent / 100) * (package1_cost + package2_cost)
    discounted_cost = package1_cost + package2_cost - discount_amount
    finale_firework_cost = 150
    total_cost = discounted_cost + finale_firework_cost
    result = total_cost
    return result

print(solution())