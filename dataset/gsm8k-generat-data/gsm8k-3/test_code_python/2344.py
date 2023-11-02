def solution():
    """Olivia's insurance premium starts out at $50/month. It goes up 10% for every accident and $5/month for every ticket. 
    If she gets in one accident and gets 3 tickets, what's her new insurance premium?"""
    # Define the starting premium and increases
    starting_premium = 50
    accident_increase = 0.1
    ticket_increase = 5

    # Calculate the premium increase due to the accident
    accident_premium_increase = starting_premium * accident_increase

    # Calculate the premium increase due to the tickets
    ticket_premium_increase = 3 * ticket_increase

    # Calculate the new premium
    new_premium = starting_premium + accident_premium_increase + ticket_premium_increase

    # Display the new premium
    result = new_premium
    return result

print(solution())