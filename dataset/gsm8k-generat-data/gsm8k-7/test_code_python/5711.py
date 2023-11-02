def solution():
    ticket_cost = 11
    snacks_cost = 3
    headphones_cost = 16
    hours_working_online = 0

    # Calculate the total cost of Biff's expenses
    total_expenses = ticket_cost + snacks_cost + headphones_cost

    # Calculate the total cost of using the bus's WiFi for the entire trip
    wifi_cost = 2 * hours_working_online

    # Calculate the total amount of money Biff can earn by working online during the trip
    earning = 12 * hours_working_online

    # Calculate the number of hours Biff needs to work to break even
    hours_break_even = (total_expenses + wifi_cost) / (12 - 2)

    result = hours_break_even
    return result

print(solution())