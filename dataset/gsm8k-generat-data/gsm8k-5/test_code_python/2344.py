def solution():
    base_premium = 50  # Olivia's starting insurance premium is $50/month
    accident_increase = 0.1  # Her premium increases 10% per accident
    ticket_increase = 5  # Her premium increases $5/month per ticket
    num_accidents = 1  # Olivia gets in one accident
    num_tickets = 3  # Olivia receives 3 tickets

    # Calculate the total increase in premium due to accidents
    accident_premium_increase = base_premium * accident_increase * num_accidents

    # Calculate the total increase in premium due to tickets
    ticket_premium_increase = num_tickets * ticket_increase

    # Add the base premium and the total premium increases to get the new premium
    new_premium = base_premium + accident_premium_increase + ticket_premium_increase
    result = new_premium
    return result

print(solution())