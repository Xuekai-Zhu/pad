def solution():
    """Celina enjoys hiking in the mountains. Due to a lack of proper equipment, she decided to order a new pair of boots, a flashlight, and a special hoodie. The hoodie cost $80 and the flashlight was only 20% of that price. The pair of boots cost was $110, but due to a special promotion, Celina was able to buy them 10% cheaper. How much did Celina spend in total on the above-mentioned equipment?"""
    hoodie_cost = 80
    flashlight_cost = hoodie_cost * 0.2
    boots_cost = 110 * 0.9
    total_cost = hoodie_cost + flashlight_cost + boots_cost
    result = total_cost
    return result

print(solution())