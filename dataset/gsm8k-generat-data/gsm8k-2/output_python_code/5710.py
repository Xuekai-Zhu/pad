def solution():
    """Biff is getting ready for a long bus trip. He spends $11 on the ticket, $3 on drinks and snacks, and $16 on a new pair of headphones to listen to music. Biff plans to do online tasks using the bus's WiFi during his trip. If Biff makes $12/hour working online and has to pay $2/hour to access the bus's WiFi, how many hours long will the bus ride need to be for him to break even?"""
    ticket_price = 11
    snacks_price = 3
    headphones_price = 16
    total_expenses = ticket_price + snacks_price + headphones_price
    hourly_income = 12
    hourly_wifi_cost = 2
    break_even_time = total_expenses / (hourly_income - hourly_wifi_cost)
    result = break_even_time
    return result

print(solution())