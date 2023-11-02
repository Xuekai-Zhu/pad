def solution():
    """Biff is getting ready for a long bus trip. He spends $11 on the ticket, $3 on drinks and snacks, and $16 on a new pair of headphones to listen to music. Biff plans to do online tasks using the bus's WiFi during his trip. If Biff makes $12/hour working online and has to pay $2/hour to access the bus's WiFi, how many hours long will the bus ride need to be for him to break even?"""
    # Define the total initial cost
    initial_cost = 11 + 3 + 16

    # Define the hourly income and the hourly cost of WiFi access
    hourly_income = 12
    hourly_cost = 2

    # Calculate the break-even point in terms of hours
    break_even_hours = initial_cost / (hourly_income - hourly_cost)

    result = break_even_hours
    return result

print(solution())