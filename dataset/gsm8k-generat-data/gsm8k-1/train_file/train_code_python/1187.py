def solution():
    """Preston has a sandwich shop. He charges $5 for each sandwich. He also charges $20 for a delivery fee. Abra Company orders 18 sandwiches from Preston and also tips him 10%. How much total, in dollars, did Preston receive?"""
    sandwich_price = 5
    delivery_fee = 20
    num_sandwiches = 18
    total_price = (sandwich_price * num_sandwiches) + delivery_fee
    tip_percent = 10
    tip_amount = total_price * (tip_percent / 100)
    total_received = total_price + tip_amount
    result = total_received
    return result

print(solution())