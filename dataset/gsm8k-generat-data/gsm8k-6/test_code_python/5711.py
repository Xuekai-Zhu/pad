def solution():
    # Calculate the total cost for Biff
    total_cost = 11 + 3 + 16  # cost of ticket, drinks/snacks, and headphones
    # Calculate Biff's net earnings per hour
    net_earnings_per_hour = 12 - 2  # earnings per hour minus WiFi cost per hour
    # Calculate the number of hours Biff needs to work to break even
    hours_to_break_even = total_cost / net_earnings_per_hour
    result = hours_to_break_even
    return result

print(solution())