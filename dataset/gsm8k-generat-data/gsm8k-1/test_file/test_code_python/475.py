def solution():
    """Tom decides to give his wife an anniversary getaway. The plane tickets cost $5000 each. The hotel is 20% more expensive than normal because it is a busy weekend. The normal price is $1500 per day. If they are there for 3 days how much did the trip cost?"""
    plane_ticket_cost = 5000
    hotel_normal_price = 1500
    hotel_busy_weekend_price = hotel_normal_price * 1.2
    days_staying = 3
    hotel_cost = hotel_busy_weekend_price * days_staying

    total_cost = plane_ticket_cost * 2 + hotel_cost
    result = total_cost
    return result

print(solution())