def solution():
    """Chris is trying to sell his car for $5200 and has gotten two price offers. One buyer offered to pay the full price if Chris would pay for the car maintenance inspection, which cost a tenth of Chris’s asking price. The other buyer agreed to pay the price if Chris replaced the headlights for $80 and the tires for three times as much.
    What is the difference between the amounts Chris will earn from the two offers?"""
    asking_price = 5200

    # Offer 1: Full price if Chris pays for car maintenance inspection
    inspection_cost = asking_price * 0.1
    offer1 = asking_price - inspection_cost

    # Offer 2: Full price if Chris replaced headlights and tires
    headlights_cost = 80
    tires_cost = 3 * headlights_cost
    offer2 = asking_price - headlights_cost - tires_cost

    # Calculate the difference between the two offers
    difference = abs(offer1 - offer2)

    result = difference
    return result

print(solution())