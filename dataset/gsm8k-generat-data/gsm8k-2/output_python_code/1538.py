def solution():
    """Chris is trying to sell his car for $5200 and has gotten two price offers. One buyer offered to pay the full price if Chris would pay for the car maintenance inspection, which cost a tenth of Chris’s asking price. The other buyer agreed to pay the price if Chris replaced the headlights for $80 and the tires for three times as much. What is the difference between the amounts Chris will earn from the two offers?"""
    asking_price = 5200
    inspection_cost = asking_price / 10
    offer1_price = asking_price - inspection_cost
    headlight_cost = 80
    tire_cost = 3 * headlight_cost
    offer2_price = asking_price - headlight_cost - tire_cost
    earnings_difference = offer1_price - offer2_price
    result = earnings_difference
    return result

print(solution())