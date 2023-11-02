def solution():
    num_tickets_website = 2
    num_tickets_scalper = 2
    num_tickets_friend = 1
    price_normal = 50
    scalper_percentage = 240
    scalper_discount = 10
    friend_percentage = 60
    total_tickets = num_tickets_website + num_tickets_scalper + num_tickets_friend
    scalper_payment = ((price_normal * scalper_percentage) / 100) - scalper_discount
    friend_payment = (price_normal * friend_percentage) / 100
    result = (num_tickets_website * price_normal) + scalper_payment + friend_payment
    return result

print(solution())