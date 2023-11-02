def solution():
    """Olivia's insurance premium starts out at $50/month. It goes up 10% for every accident and $5/month for every ticket. If she gets in one accident and gets 3 tickets, what's her new insurance premium?"""
    # Define the initial premium and the additional costs for accident and tickets
    initial_premium = 50
    accident_cost = 0.1
    ticket_cost = 5

    # Calculate the new premium after an accident
    new_premium = initial_premium * (1 + accident_cost)

    # Calculate the new premium after tickets
    new_premium += ticket_cost * 3

    result = new_premium
    return result

print(solution())