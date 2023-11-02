def solution():
    """Jayden had $70 from selling pictures he took as a hobby. His sister Ava gave him half of her $90 allowance to help him buy a new camera that costs $200. How much more does Jayden need to buy the camera?"""
    jayden_money = 70
    ava_money = 90 / 2
    camera_cost = 200
    total_money = jayden_money + ava_money
    money_left = camera_cost - total_money
    result = money_left
    return result

print(solution())