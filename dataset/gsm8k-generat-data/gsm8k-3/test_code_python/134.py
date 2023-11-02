def solution():
    """A couple with two children, ages 6 and 10 years old, decided to go to an amusement park. The regular ticket costs $109, but children below 12 years old have a $5 discount. If they gave the cashier $500, how much change will they receive?"""
    # Define the ticket price and the number of tickets to be purchased
    ticket_price = 109
    num_tickets = 2  # for the couple

    # Calculate the total cost of tickets for the family
    total_cost = (num_tickets * ticket_price) - (5*2)  # children get discount

    # Calculate the amount of change they will receive
    change = 500 - total_cost

    # Return the result
    result = change
    return result

print(solution())