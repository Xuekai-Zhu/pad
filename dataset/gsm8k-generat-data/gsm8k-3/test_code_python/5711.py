def solution():
    """Biff is getting ready for a long bus trip. He spends $11 on the ticket, $3 on drinks and snacks, and $16 on a new pair of headphones to listen to music. Biff plans to do online tasks using the bus's WiFi during his trip. If Biff makes $12/hour working online and has to pay $2/hour to access the bus's WiFi, how many hours long will the bus ride need to be for him to break even?"""
    # Define the costs and earnings for Biff's bus trip
    TICKET_COST = 11
    SNACKS_COST = 3
    HEADPHONES_COST = 16
    WIFI_COST = 2
    ONLINE_EARNINGS = 12

    # Calculate the total cost of the trip
    total_cost = TICKET_COST + SNACKS_COST + HEADPHONES_COST

    # Calculate the net earnings per hour
    net_earnings = ONLINE_EARNINGS - WIFI_COST

    # Calculate the break-even point in hours
    break_even_hours = total_cost / net_earnings

    # Display the break-even point
    result = break_even_hours
    return result

print(solution())