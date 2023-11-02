def solution():
    # Calculate the total cost for Biff's bus trip
    total_cost = 11 + 3 + 16  # $11 for the ticket, $3 for drinks and snacks, $16 for headphones

    # Calculate the total amount Biff earns while working online during the bus ride
    hourly_profit = 12 - 2  # Biff earns $12/hour but pays $2/hour for WiFi access
    total_profit = hourly_profit * hours

    # Calculate the hours of bus ride needed for Biff to break even
    hours_needed = total_cost / total_profit
    result = hours_needed
    return result

print(solution())